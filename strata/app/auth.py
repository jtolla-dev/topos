import secrets
from uuid import UUID

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Tenant

security = HTTPBearer()


def hash_api_key(api_key: str) -> str:
    """Hash an API key using bcrypt."""
    return bcrypt.hashpw(api_key.encode(), bcrypt.gensalt()).decode()


def verify_api_key(api_key: str, hashed: str) -> bool:
    """Verify an API key against its hash."""
    return bcrypt.checkpw(api_key.encode(), hashed.encode())


def generate_api_key() -> str:
    """Generate a secure random API key."""
    return f"strata_{secrets.token_urlsafe(32)}"


async def get_current_tenant(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: AsyncSession = Depends(get_session),
) -> Tenant:
    """
    Authenticate request using Bearer token and return the associated tenant.

    For v0, we do a simple lookup by trying all tenant API keys.
    In production, you'd use a proper token system or cache.
    """
    api_key = credentials.credentials

    # Get all tenants and check API keys
    result = await session.execute(select(Tenant))
    tenants = result.scalars().all()

    for tenant in tenants:
        if verify_api_key(api_key, tenant.api_key_hash):
            return tenant

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API key",
        headers={"WWW-Authenticate": "Bearer"},
    )


class TenantContext:
    """Context object containing the authenticated tenant and session."""

    def __init__(self, tenant: Tenant, session: AsyncSession):
        self.tenant = tenant
        self.session = session

    @property
    def tenant_id(self) -> UUID:
        return self.tenant.id


async def get_tenant_context(
    tenant: Tenant = Depends(get_current_tenant),
    session: AsyncSession = Depends(get_session),
) -> TenantContext:
    """Get a tenant context with both tenant and session."""
    return TenantContext(tenant=tenant, session=session)
