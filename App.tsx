import React, { useState, useEffect, useRef } from 'react';
import { motion, useScroll, useTransform, AnimatePresence, useSpring } from 'framer-motion';
import { 
  Menu, X, ArrowDown, Bug, Quote, AlertTriangle, MousePointer2, RefreshCw, 
  BarChart, FileText, Shield, Target, Sparkles, Instagram, Linkedin, 
  ArrowUpRight, Dna, Lightbulb, ShieldCheck, Brain, MessageSquare, 
  Cpu, Lock, Star, Activity
} from 'lucide-react';

/* --- COMPONENTE LETRA 'i' COM QUADRADO (Sincronia Total) --- */
function LetterI({ size = "text-2xl", color = "text-accent" }) {
  return (
    <span className={`relative inline-block leading-none ${color} ${size}`}>
      i
      <span 
        className="absolute bg-current shadow-[0_0_15px_rgba(220,38,38,0.4)]"
        style={{
          width: '0.22em',
          height: '0.22em',
          top: '-0.15em',
          left: '0.05em',
          transform: 'rotate(10deg)',
        }}
      ></span>
    </span>
  );
}

/* --- LOGO ORIGINAL (INCLINADA + QUADRADO NO i) --- */
function Logo({ className = "" }) {
  return (
    <div className={`font-display font-black text-2xl tracking-tighter italic flex items-center select-none ${className}`}>
      <span className="text-white">NA</span>
      <span className="text-accent ml-1 flex items-baseline">
        VE
        <LetterI size="text-2xl" />
        A
      </span>
    </div>
  );
}

function MagneticButton({ children, className = "", onClick, href, target, rel, disabled }: { children: React.ReactNode, className?: string, onClick?: () => void, href?: string, target?: string, rel?: string, disabled?: boolean }) {
  const buttonRef = useRef<HTMLButtonElement | HTMLAnchorElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e: React.MouseEvent<HTMLElement>) => {
    if (!buttonRef.current || disabled) return;
    const { clientX, clientY } = e;
    const { left, top, width, height } = buttonRef.current.getBoundingClientRect();
    const x = (clientX - (left + width / 2)) * 0.3;
    const y = (clientY - (top + height / 2)) * 0.3;
    setPosition({ x, y });
  };

  const handleMouseLeave = () => {
    setPosition({ x: 0, y: 0 });
  };

  const commonProps = {
    className: `relative inline-flex items-center justify-center transition-transform duration-300 ease-out ${className}`,
    onMouseMove: handleMouseMove,
    onMouseLeave: handleMouseLeave,
    style: { transform: `translate(${position.x}px, ${position.y}px)` }
  };

  if (href) {
    return (
      <a href={href} ref={buttonRef as React.RefObject<HTMLAnchorElement>} target={target} rel={rel} {...commonProps}>
        {children}
      </a>
    );
  }

  return (
    <button ref={buttonRef as React.RefObject<HTMLButtonElement>} onClick={onClick} disabled={disabled} {...commonProps}>
      {children}
    </button>
  );
}

function TiltCard({ children, className = "" }: { children: React.ReactNode, className?: string }) {
  const cardRef = useRef<HTMLDivElement>(null);
  const [rotateX, setRotateX] = useState(0);
  const [rotateY, setRotateY] = useState(0);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!cardRef.current) return;
    const { left, top, width, height } = cardRef.current.getBoundingClientRect();
    const x = e.clientX - left;
    const y = e.clientY - top;
    const centerX = width / 2;
    const centerY = height / 2;
    const rotateXValue = ((y - centerY) / centerY) * -10;
    const rotateYValue = ((x - centerX) / centerX) * 10;
    setRotateX(rotateXValue);
    setRotateY(rotateYValue);
  };

  const handleMouseLeave = () => {
    setRotateX(0);
    setRotateY(0);
  };

  return (
    <motion.div
      ref={cardRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      animate={{ rotateX, rotateY }}
      transition={{ type: "spring", stiffness: 300, damping: 30, mass: 0.5 }}
      style={{ transformStyle: "preserve-3d", perspective: "1000px" }}
      className={`relative w-full h-full ${className}`}
    >
      <div style={{ transform: "translateZ(30px)", transformStyle: "preserve-3d" }} className="w-full h-full">
        {children}
      </div>
    </motion.div>
  );
}

function CustomCursor() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [isHovering, setIsHovering] = useState(false);

  useEffect(() => {
    const updateMousePosition = (e: MouseEvent) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };
    const handleMouseOver = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (target.tagName.toLowerCase() === 'a' || target.tagName.toLowerCase() === 'button' || target.closest('a') || target.closest('button')) {
        setIsHovering(true);
      } else {
        setIsHovering(false);
      }
    };
    window.addEventListener('mousemove', updateMousePosition);
    window.addEventListener('mouseover', handleMouseOver);
    return () => {
      window.removeEventListener('mousemove', updateMousePosition);
      window.removeEventListener('mouseover', handleMouseOver);
    };
  }, []);

  return (
    <div className="hidden lg:block pointer-events-none">
      <motion.div
        className="fixed top-0 left-0 w-3 h-3 bg-accent rounded-full z-[100] mix-blend-screen"
        animate={{ x: mousePosition.x - 6, y: mousePosition.y - 6, scale: isHovering ? 2.5 : 1 }}
        transition={{ type: 'spring', stiffness: 500, damping: 28 }}
      />
      <motion.div
        className="fixed top-0 left-0 w-8 h-8 border border-accent/50 rounded-full z-[100] mix-blend-screen"
        animate={{ x: mousePosition.x - 16, y: mousePosition.y - 16, scale: isHovering ? 1.5 : 1 }}
        transition={{ type: 'spring', stiffness: 250, damping: 20 }}
      />
    </div>
  );
}

function Hero() {
  const { scrollY } = useScroll();
  const y = useTransform(scrollY, [0, 1000], [0, 300]);
  const opacity = useTransform(scrollY, [0, 500], [0.6, 0]);
  
  return (
    <div id="hero" className="relative min-h-screen w-full overflow-hidden flex flex-col items-center justify-center bg-[#050505] pt-32 pb-20">
      <motion.div style={{ y, opacity }} className="absolute inset-0 z-0">
        <img 
          src="assets/hero.bg.jpg" 
          alt="NA VEiA Hero" 
          className="w-full h-full object-cover opacity-60 mix-blend-luminosity"
          style={{ 
            maskImage: 'linear-gradient(to bottom, black 50%, transparent 100%)',
            WebkitMaskImage: 'linear-gradient(to bottom, black 50%, transparent 100%)'
          }}
        />
      </motion.div>

      <div className="relative z-10 flex flex-col items-center w-full max-w-7xl mx-auto px-6 text-center">
        {/* TITULO NA EM CIMA */}
        <motion.span 
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 0.9, y: 0 }}
          className="text-[clamp(100px,25vw,280px)] font-display font-black italic leading-none text-white tracking-tighter select-none mb-4"
        >
          NA
        </motion.span>

        {/* SUBTITULO IMPACTANTE NO MEIO */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          className="max-w-2xl px-4 my-8 z-20"
        >
          <p className="text-xl md:text-2xl font-light leading-relaxed text-white/95 drop-shadow-lg">
            Fusão estratégica entre <span className="text-white font-bold border-b-2 border-accent">Neurociência</span>, <span className="text-white font-bold border-b-2 border-accent">IA Generativa</span> e <span className="text-white font-bold border-b-2 border-accent">Ciência da Criatividade</span>.
          </p>
        </motion.div>

        {/* TITULO VEIA EM BAIXO */}
        <motion.div 
          initial={{ opacity: 0, y: -50 }}
          whileInView={{ opacity: 0.9, y: 0 }}
          transition={{ delay: 0.1 }}
          className="flex items-center text-[clamp(100px,25vw,280px)] font-display font-black italic leading-none text-accent tracking-tighter select-none drop-shadow-[0_0_50px_rgba(220,38,38,0.4)]"
        >
          VE<LetterI size="text-[clamp(100px,25vw,280px)]" />A
        </motion.div>

        {/* BOTÃO ABAIXO DE TUDO */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="mt-16"
        >
          <MagneticButton href="#problem" className="flex items-center gap-4 bg-white text-black px-10 py-5 rounded-full font-bold tracking-widest uppercase text-sm hover:scale-105 transition-all shadow-xl group">
            Mapear Gargalos
            <ArrowDown className="w-5 h-5 group-hover:translate-y-2 transition-transform" />
          </MagneticButton>
        </motion.div>
      </div>
    </div>
  );
}

const Footer = () => (
  <footer className="py-12 bg-[#050505] border-t border-white/10 text-center">
    <Logo className="justify-center mb-6" />
    <p className="text-neutral-500 text-[11px] font-tech uppercase tracking-widest">© 2025 Vitalino | NA VEiA. All_Rights_Reserved.</p>
  </footer>
);

export default function App() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30 });

  return (
    <div className="min-h-screen bg-background text-white font-sans selection:bg-accent/30 lg:cursor-none relative overflow-x-hidden">
      <CustomCursor />
      <motion.div className="fixed top-0 left-0 right-0 h-1 bg-accent origin-left z-[60]" style={{ scaleX }} />
      <Hero />
      <Footer />
    </div>
  );
}
