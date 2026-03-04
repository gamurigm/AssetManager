export default function Loading() {
  return (
    <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-black">
      {/* Background image — semi-transparent */}
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-60"
        style={{ backgroundImage: "url('/fondo-bg1.jpg')" }}
      />

      {/* Dark vignette overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/60 via-transparent to-black/80" />

      {/* Content */}
      <div className="relative z-10 flex flex-col items-center gap-6">
        {/* Logo / Brand */}
        <div className="flex items-center gap-3">
          <img
            src="/logoMM.png"
            alt="MMAM"
            className="h-12 w-12 object-contain"
          />
          <span className="text-2xl font-bold tracking-[0.2em] text-white/90 uppercase">
            MMAM Intelligence
          </span>
        </div>

        {/* Spinner */}
        <div className="relative h-10 w-10">
          <div className="absolute inset-0 rounded-full border-2 border-white/10" />
          <div className="absolute inset-0 rounded-full border-2 border-t-cyan-400 border-r-transparent border-b-transparent border-l-transparent animate-spin" />
        </div>

        {/* Loading text */}
        <p className="text-xs tracking-[0.3em] uppercase text-white/40 animate-pulse">
          Loading systems
        </p>
      </div>
    </div>
  );
}
