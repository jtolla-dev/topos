import { cn } from '@/lib/client/utils/cn'

interface LogoProps {
  className?: string
  showText?: boolean
}

export function LogoMark({ className }: { className?: string }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 128 128"
      aria-label="Topos logo mark"
      role="img"
      className={className}
      fill="currentColor"
    >
      <g>
        {/* 4 nodes */}
        <circle cx="64" cy="28" r="18" />
        <circle cx="28" cy="64" r="18" />
        <circle cx="100" cy="64" r="18" />
        <circle cx="64" cy="100" r="18" />

        {/* 4 connectors (rotated squares) */}
        <rect x="40" y="40" width="8" height="8" transform="rotate(45 44 44)" />
        <rect x="80" y="40" width="8" height="8" transform="rotate(45 84 44)" />
        <rect x="40" y="80" width="8" height="8" transform="rotate(45 44 84)" />
        <rect x="80" y="80" width="8" height="8" transform="rotate(45 84 84)" />
      </g>
    </svg>
  )
}

export function Logo({ className, showText = true }: LogoProps) {
  return (
    <span className={cn('inline-flex items-center gap-2 font-bold', className)}>
      <LogoMark className="h-[1.2em] w-[1.2em]" />
      {showText && 'Topos'}
    </span>
  )
}
