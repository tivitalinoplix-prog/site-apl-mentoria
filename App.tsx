import React, { useState, useEffect, useRef } from 'react';
import { motion, useScroll, useTransform, AnimatePresence, useSpring } from 'framer-motion';
import { 
  Menu, X, ArrowDown, Bug, Quote, AlertTriangle, MousePointer2, RefreshCw, 
  BarChart, FileText, Shield, Target, Sparkles, Instagram, Linkedin, 
  ArrowUpRight, Dna, Lightbulb, ShieldCheck, Brain, MessageSquare, 
  Cpu, Lock, Star, Activity
} from 'lucide-react';

/* --- LOGO ORIGINAL (INCLINADA + QUADRADO NO i) --- */
function Logo({ className = "" }) {
  return (
    <div className={`font-display font-black text-2xl tracking-tighter italic flex items-center select-none ${className}`}>
      <span className="text-white">NA</span>
      <span className="text-accent ml-1 flex items-baseline relative">
        VE
        <span className="relative inline-block leading-none">
          i
          <span className="absolute top-[-3px] left-[-0.5px] w-[5px] h-[5px] bg-accent rotate-[10deg] shadow-[0_0_10px_rgba(220,38,38,0.6)]"></span>
        </span>
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
  const xLeft = useTransform(scrollY, [0, 1000], [0, -300]);
  const xRight = useTransform(scrollY, [0, 1000], [0, 300]);

  return (
    <div id="hero" className="relative h-screen w-full overflow-hidden flex items-center justify-center pt-20 bg-[#050505]">
      {/* RESTORED HERO PHOTO BEHAVIOR */}
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

      <div className="relative z-10 flex flex-col lg:flex-row w-full max-w-7xl mx-auto px-6 items-center justify-center">
        <motion.div style={{ x: xLeft }} className="flex-1 flex justify-center lg:justify-end lg:pr-8">
          <span className="text-[clamp(100px,20vw,240px)] font-display font-black italic leading-none text-white tracking-tighter opacity-90">NA</span>
        </motion.div>
        <motion.div style={{ x: xRight }} className="flex-1 flex justify-center lg:justify-start lg:pl-8">
          <div className="relative">
            <span className="text-[clamp(100px,20vw,240px)] font-display font-black italic leading-none text-accent tracking-tighter opacity-90 drop-shadow-[0_0_40px_rgba(220,38,38,0.5)]">VEiA</span>
            <div className="absolute top-[20%] left-[54%] w-[clamp(20px,4vw,50px)] h-[clamp(20px,4vw,50px)] bg-accent rotate-[12deg] shadow-[0_0_60px_rgba(220,38,38,0.6)]"></div>
          </div>
        </motion.div>
      </div>

      <div className="absolute bottom-12 left-0 right-0 flex flex-col items-center justify-center z-20">
        <p className="text-base font-light text-neutral-400 mb-8 max-w-md text-center px-4">
          Fusão estratégica entre <span className="text-white font-medium">Neurociência</span>, <span className="text-white font-medium">IA Generativa</span> e <span className="text-white font-medium">Ciência da Criatividade</span>.
        </p>
        <MagneticButton href="#problem" className="flex items-center gap-3 bg-white text-black px-8 py-4 rounded-full font-semibold tracking-wide hover:bg-gray-200 uppercase text-sm group">
          Mapear Gargalos
          <ArrowDown className="w-5 h-5 group-hover:translate-y-1 transition-transform" />
        </MagneticButton>
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
