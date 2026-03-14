<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth bg-[#080808]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vitalino — NA VEiA | Engenharia de Conhecimento e IA</title>
    <meta name="description" content="Engenharia de Conhecimento e Automação de Processos com a fusão de Neurociência, Criatividade e IA Aplicada.">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Manrope:wght@200;400;700;800&family=Orbitron:wght@400;600;900&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS (CDN) -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
    
    <!-- Tailwind Configuration -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        display: ['Manrope', 'sans-serif'],
                        tech: ['Orbitron', 'sans-serif'],
                    },
                    colors: {
                        background: '#080808',
                        surface: '#0d0d0d',
                        card: '#111111',
                        border: 'rgba(255, 42, 42, 0.12)',
                        primary: '#f0f0f0',
                        secondary: '#888888',
                        accent: '#ff2a2a',
                        'accent-soft': 'rgba(255, 42, 42, 0.15)',
                    }
                }
            }
        }
    </script>
    
    <style>
        body { 
            background-color: #080808; 
            color: #f0f0f0; 
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            font-family: 'Inter', sans-serif;
        }

        /* NATIVE SELECTION */
        ::selection { background: rgba(255,42,42,0.3); color: white; }

        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #080808; }
        ::-webkit-scrollbar-thumb { background: #111111; border-radius: 2px; }
        ::-webkit-scrollbar-thumb:hover { background: #ff2a2a; }

        .text-glow-red { text-shadow: 0 0 20px rgba(255, 42, 42, 0.3); }

        /* PRELOADER DOOR EFFECT */
        #preloader { perspective: 1000px; display: flex; width: 100vw; height: 100vh; position: fixed; top: 0; left: 0; z-index: 100; pointer-events: none; }
        .door-left, .door-right { 
            width: 50%; height: 100%; background: #080808; position: relative;
            transition: transform 0.9s cubic-bezier(0.76, 0, 0.24, 1); will-change: transform; 
            overflow: hidden; pointer-events: auto;
        }
        .door-left { border-right: 1px solid rgba(255, 42, 42, 0.15); }
        .door-right { border-left: 1px solid rgba(255, 42, 42, 0.15); }

        .door-open-left { transform: translateX(-100%); }
        .door-open-right { transform: translateX(100%); }
        .scanline {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to bottom, transparent 50%, rgba(255,255,255,0.03) 51%, transparent 51%);
            background-size: 100% 4px; pointer-events: none; z-index: 10;
        }

        /* SCROLL REVEAL GLOBAL */
        .reveal-element { 
            opacity: 0; 
            transform: translateY(20px); 
            transition: opacity 0.7s ease, transform 0.7s ease; 
        }
        .reveal-element.is-visible { 
            opacity: 1; 
            transform: translateY(0); 
        }
        .reveal-right {
            opacity: 0; 
            transform: translateX(40px); 
            transition: opacity 0.7s ease, transform 0.7s ease; 
        }
        .reveal-right.is-visible {
            opacity: 1; 
            transform: translateX(0); 
        }

        /* ICON REVEAL EFFECT */
        .icon-reveal {
            opacity: 0;
            transform: scale(0) rotate(-180deg);
            transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.5s ease;
        }
        .is-visible .icon-reveal, .icon-reveal.is-visible {
            opacity: 1;
            transform: scale(1) rotate(0deg);
        }

        /* HERO */
        .text-hero { font-size: clamp(60px, 18vw, 240px); line-height: 0.8; user-select: none; }
        .text-hero-mobile { font-size: clamp(80px, 22vw, 140px); line-height: 0.8; user-select: none; }

        /* SECTION: METHOD / 3 PILARES */
        .method-grid {
            display: grid;
            grid-template-columns: repeat(1, 1fr);
            gap: 2rem;
        }
        @media (min-width: 768px) { .method-grid { grid-template-columns: repeat(2, 1fr); } }
        
        .method-card {
            background: #111111;
            border: 1px solid rgba(255, 42, 42, 0.12);
            border-radius: 2px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.4s ease;
        }
        .method-card:hover {
            transform: translateY(-4px);
            border-color: rgba(255, 42, 42, 0.4);
            box-shadow: 0 8px 32px rgba(255, 42, 42, 0.08);
        }
        .method-card:hover .icon-reveal {
            transform: translateY(-3px);
            color: #ff2a2a;
        }
        .watermark {
            font-size: clamp(5rem, 10vw, 8rem);
            color: #ff2a2a;
            opacity: 0.06;
            position: absolute;
            top: -1rem; right: 1rem;
            font-weight: 900;
            line-height: 1;
            pointer-events: none;
        }
        .method-tag {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.7rem;
            color: #f0f0f0;
            border: 1px solid rgba(255, 42, 42, 0.3);
            padding: 2px 8px;
            display: inline-block;
            margin-bottom: 1rem;
            text-transform: uppercase;
        }
        .method-progress-line {
            width: 2px; background: #ff2a2a; transition: height 0.1s;
            position: absolute; left: -1rem; top: 0; bottom: 0; height: 0%;
        }

        /* GARGALOS (PROBLEM) CARDS */
        .gargalo-card {
            background: #111111;
            border: 1px solid rgba(255,42,42,0.12);
            border-radius: 2px;
            padding: 20px 24px;
            display: flex;
            align-items: flex-start;
            gap: 16px;
            margin-bottom: 12px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .gargalo-card:hover {
            border-color: rgba(255,42,42,0.4);
            background: #150f0f;
            transform: translateX(6px);
        }
        .gargalo-card:hover .icon-reveal {
            transform: translateY(-3px);
            color: #ff2a2a;
        }
        .gargalo-card.estagnacao {
            border-color: rgba(255,42,42,0.4);
            background: rgba(255,42,42,0.05);
        }
        .gargalo-card.estagnacao:hover {
            box-shadow: 0 0 20px rgba(255,42,42,0.15);
        }
        .pulse-icon {
            animation: pulseShadow 2s infinite;
            border-radius: 50%;
        }
        @keyframes pulseShadow {
            0% { box-shadow: 0 0 0 0 rgba(255, 42, 42, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(255, 42, 42, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 42, 42, 0); }
        }

        /* ESPECIALISTA IMAGE EFFECT */
        #mentor-img {
            filter: grayscale(100%) contrast(1.1) brightness(0.9);
            transition: filter 0.6s ease;
            position: relative;
        }
        #mentor-img-wrapper:hover #mentor-img {
            filter: grayscale(0%) contrast(1.1) brightness(1);
        }
        #mentor-img-wrapper {
            position: relative;
            overflow: hidden;
        }
        #mentor-img-wrapper::after {
            content: '';
            position: absolute;
            left: 0; right: 0; bottom: 0; height: 50%;
            background: linear-gradient(to top, #080808 0%, transparent 100%);
            pointer-events: none;
        }
        .scanner-line {
            position: absolute;
            top: -100%; left: 0; width: 100%; height: 2px;
            background: #ff2a2a;
            opacity: 0.15;
            box-shadow: 0 0 10px #ff2a2a;
            animation: scanAnim 3s linear infinite;
            z-index: 20;
            pointer-events: none;
        }
        @keyframes scanAnim {
            0% { top: -10%; }
            100% { top: 110%; }
        }
        .auth-key-tag {
            position: absolute;
            top: 1rem; left: 1rem;
            background: rgba(0,0,0,0.7);
            color: #ff2a2a;
            font-family: inherit;
            font-size: 0.75rem;
            padding: 4px 8px;
            z-index: 30;
            border-radius: 2px;
            backdrop-filter: blur(4px);
        }

        /* BUTTONS */
        .btn-primary {
            background-color: #ff2a2a;
            color: #ffffff;
            transition: all 0.3s ease;
            border: 1px solid transparent;
        }
        .btn-primary:hover {
            filter: brightness(1.15);
            transform: scale(1.02);
            border-color: rgba(255,255,255,0.2);
        }
        
    </style>
</head>
<body class="bg-[#080808]">

    <!-- Preloader Porta Dupla -->
    <div id="preloader" class="fixed inset-0 z-[100] flex w-full h-full">
        <div id="door-left" class="door-left border-r border-[#1a1a1a]">
            <div class="scanline"></div>
        </div>
        <div id="door-right" class="door-right border-l border-[#1a1a1a]">
            <div class="scanline"></div>
        </div>
        <div id="preloader-content" class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none z-10 transition-opacity duration-300">
            <span class="font-display font-black text-4xl md:text-6xl text-white tracking-tighter">NA <span class="text-[#ff2a2a]">VEiA</span></span>
            <span class="font-tech text-xs tracking-widest text-[#ff2a2a] mt-4 uppercase animate-pulse">_System_Boot</span>
        </div>
    </div>

    <!-- Navigation -->
    <nav class="absolute top-0 inset-x-0 z-50 w-full flex justify-between items-center p-6 lg:px-8 lg:py-8 text-sm font-normal tracking-wide bg-transparent border-b border-[rgba(255,42,42,0.12)]">
        <div class="font-display font-black text-xl tracking-tighter text-white uppercase">VITALINO<span class="text-[#ff2a2a]">.</span></div>
        <div class="hidden lg:flex gap-6 items-center">
            <a href="#problem" class="text-[#888888] hover:text-[#f0f0f0] transition-colors font-tech text-[10px] tracking-widest uppercase">Gargalos</a>
            <a href="#method" class="text-[#888888] hover:text-[#f0f0f0] transition-colors font-tech text-[10px] tracking-widest uppercase">Método</a>
            <a href="#mentor" class="text-[#888888] hover:text-[#f0f0f0] transition-colors font-tech text-[10px] tracking-widest uppercase">Especialista</a>
        </div>
        <div class="flex gap-6 items-center">
            <div class="hidden lg:flex items-center gap-2 border border-[rgba(255,42,42,0.12)] px-3 py-1.5 rounded-sm bg-[#111111]">
                <div class="w-1.5 h-1.5 rounded-full bg-[#ff2a2a] animate-pulse glow-dot shadow-[0_0_8px_rgba(255,42,42,0.8)]"></div>
                <span class="font-tech text-[8px] tracking-widest text-[#ff2a2a] uppercase">System_Active</span>
            </div>
            <a href="#ai-consultant" class="hidden lg:block text-[#ff2a2a] font-tech text-[10px] tracking-widest uppercase hover:text-white transition-colors">Diagnóstico</a>
        </div>
    </nav>

    <!-- Main Grid Layout (HERO) -->
    <div class="relative z-10 w-full min-h-[90vh] grid grid-cols-1 lg:grid-cols-4 pointer-events-none pt-24 lg:pt-0 border-b border-[rgba(255,42,42,0.12)]">
        <!-- MOBILE ONLY Hero Section -->
        <div class="lg:hidden col-span-1 flex flex-col justify-center px-6 pointer-events-auto mt-20 mb-12">
             <div class="w-full select-none flex justify-between reveal-element">
                 <span class="text-hero-mobile font-display font-[900] tracking-tighter text-[#f0f0f0] block">NA</span>
                 <span class="text-hero-mobile font-display font-[900] tracking-tighter text-[#ff2a2a] block text-right">VEiA</span>
            </div>
        </div>

        <!-- Column 1 -->
        <div class="h-full border-[rgba(255,42,42,0.12)] flex flex-col justify-between relative pointer-events-auto min-h-0 lg:min-h-screen lg:border-r">
            <div class="hidden lg:block absolute top-28 left-0 w-[200%] pointer-events-none select-none z-[60] px-[1vw] overflow-visible reveal-element">
                 <span class="text-hero font-display font-[900] tracking-tighter text-[#f0f0f0] block whitespace-nowrap pl-4 lg:pl-0">NA</span>
            </div>
            <div class="relative lg:absolute lg:top-[40%] left-0 w-full px-6 lg:px-8 z-[70] flex flex-col gap-6 mb-12 lg:mb-0 reveal-element" style="transition-delay: 0.2s;">
                <div class="relative w-full aspect-[3/2] bg-[#111111] border border-[rgba(255,42,42,0.12)] rounded-sm flex items-center justify-center p-6 text-center">
                    <span class="px-2 py-1 bg-[#1a1a1a] border border-[#ff2a2a]/20 text-[9px] font-tech text-[#ff2a2a] tracking-widest uppercase rounded-sm absolute top-4 left-4">_Framework</span>
                    <p class="text-[13px] font-light opacity-90 leading-relaxed text-[#888888]">
                        Fusão estratégica entre <span class="text-[#f0f0f0] font-medium">Neurociência</span>, <span class="text-[#f0f0f0] font-medium">IA Generativa</span> e <span class="text-[#f0f0f0] font-medium">Ciência da Criatividade</span> para automatizar processos.
                    </p>
                </div>
            </div>
            <a href="#problem" class="w-full h-24 bg-[#111111] flex items-center justify-center text-[#f0f0f0] cursor-pointer hover:bg-[#1a1a1a] transition-colors lg:mt-auto border-t border-[rgba(255,42,42,0.12)] pointer-events-auto group">
                <span class="text-[10px] font-tech font-bold uppercase tracking-widest mr-3 text-[#ff2a2a]">Mapear Gargalos</span>
                <i data-lucide="arrow-down" class="w-4 h-4 text-[#ff2a2a] group-hover:translate-y-1 transition-transform"></i>
            </a>
        </div>

        <div class="hidden lg:block h-full border-r border-[rgba(255,42,42,0.12)] relative"></div>
        <div class="hidden lg:block h-full border-r border-[rgba(255,42,42,0.12)] relative"></div>

        <!-- Column 4 -->
        <div class="h-full relative pointer-events-auto flex flex-col justify-end border-r lg:border-none border-[rgba(255,42,42,0.12)] min-h-0 lg:min-h-screen">
             <div class="hidden lg:block absolute top-28 right-0 lg:w-[200%] pointer-events-none select-none z-[60] px-[1vw] text-right overflow-visible reveal-element">
                 <span class="text-hero font-display font-[900] tracking-tighter text-[#ff2a2a] block pr-4 lg:pr-0">VEiA</span>
            </div>
            <div class="relative lg:absolute lg:top-[40%] right-0 w-full px-6 lg:px-8 text-right z-30 mt-12 lg:mb-24 reveal-element" style="transition-delay: 0.3s;">
                <div class="flex flex-col items-end gap-1">
                    <span class="text-5xl font-light tracking-tighter flex items-start gap-1 text-[#f0f0f0]">
                        <span class="opacity-30 text-3xl font-light mt-1 text-[#ff2a2a]">/</span>
                        99.8%
                    </span>
                    <div class="mt-2 text-[9px] font-tech text-[#ff2a2a] tracking-widest uppercase opacity-90 leading-normal border-t border-[rgba(255,42,42,0.12)] pt-2 ml-auto w-32 content-end">
                        Precision Rate
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Seção Problema -->
    <section id="problem" class="relative z-20 w-full border-t border-[rgba(255,42,42,0.12)] bg-[#0d0d0d] overflow-hidden">
        <div class="grid grid-cols-1 lg:grid-cols-2 w-full max-w-[1400px] mx-auto px-6 lg:px-12 py-24 gap-16">
            <div class="flex flex-col reveal-element">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-sm border border-[rgba(255,42,42,0.2)] mb-8 bg-[#111] max-w-fit">
                    <i data-lucide="search" class="w-4 h-4 text-[#f0f0f0]"></i>
                    <span class="text-xs font-tech tracking-wide text-[#f0f0f0] uppercase">_Diagnóstico</span>
                </div>
                <h2 class="text-5xl lg:text-7xl font-display font-medium tracking-tighter text-[#f0f0f0] leading-[0.95] max-w-lg mb-6 uppercase">
                    Sua operação está <span class="text-[#ff2a2a] italic font-light normal-case block">Drenando crescimento?</span>
                </h2>
                <p class="text-xl text-[#888888] font-light leading-relaxed mb-8">
                    Empresas investem tempo e dinheiro em operações repetitivas. Documentos são redigidos manualmente e a equipe gasta horas em tarefas que deveriam ser automatizadas.
                </p>
            </div>

            <div class="flex flex-col gap-4">
                <div class="gargalo-card reveal-element" style="transition-delay: 0.1s;">
                    <i data-lucide="repeat" class="w-6 h-6 text-[#888] icon-reveal"></i>
                    <div>
                        <h4 class="text-lg font-medium text-[#f0f0f0]">Processos Manuais</h4>
                        <p class="text-sm text-[#888]">Equipe executa tarefas repetitivas sem automação.</p>
                    </div>
                </div>
                <div class="gargalo-card reveal-element" style="transition-delay: 0.2s;">
                    <i data-lucide="file-x" class="w-6 h-6 text-[#888] icon-reveal"></i>
                    <div>
                        <h4 class="text-lg font-medium text-[#f0f0f0]">Documentação Desestruturada</h4>
                        <p class="text-sm text-[#888]">Relatórios e documentos sem padrão e lentos para produzir.</p>
                    </div>
                </div>
                <div class="gargalo-card reveal-element" style="transition-delay: 0.3s;">
                    <i data-lucide="git-branch" class="w-6 h-6 text-[#888] icon-reveal"></i>
                    <div>
                        <h4 class="text-lg font-medium text-[#f0f0f0]">Gargalos de Back-office</h4>
                        <p class="text-sm text-[#888]">Operações internas travam a escala da empresa.</p>
                    </div>
                </div>
                <div class="gargalo-card reveal-element" style="transition-delay: 0.4s;">
                    <i data-lucide="brain-circuit" class="w-6 h-6 text-[#888] icon-reveal"></i>
                    <div>
                        <h4 class="text-lg font-medium text-[#f0f0f0]">IA sem Alinhamento</h4>
                        <p class="text-sm text-[#888]">Ferramentas que geram alucinações e não confiáveis.</p>
                    </div>
                </div>
                <div class="gargalo-card estagnacao reveal-element" style="transition-delay: 0.5s;">
                    <i data-lucide="alert-triangle" class="w-6 h-6 text-[#ff2a2a] icon-reveal pulse-icon"></i>
                    <div>
                        <h4 class="text-lg font-medium text-[#ff2a2a] tracking-wider uppercase">Estagnação</h4>
                        <p class="text-sm text-[#888]">Sem IA correta, a empresa perde competitividade severa.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Seção Método 3 Pilares -->
    <section id="method" class="relative z-20 w-full border-t border-[rgba(255,42,42,0.12)] bg-[#080808]">
        <div class="max-w-[1400px] mx-auto px-6 lg:px-12 py-24 relative pl-8 lg:pl-16">
            <div class="method-progress-line"></div>
            <div class="reveal-element mb-16">
                <span class="font-tech uppercase mb-4 block text-[#ff2a2a] tracking-widest text-[10px]">_THE_FRAMEWORK</span>
                <h2 class="text-4xl lg:text-7xl font-display font-black tracking-tighter text-[#f0f0f0] mb-6 leading-[0.9] uppercase">
                    O MÉTODO NA VEiA
                </h2>
                <p class="text-[#888888] text-lg max-w-xl font-light">
                    Precisão técnica absoluta para escalar seu negócio com estruturação automatizada e IA Aplicada.
                </p>
            </div>

            <div class="method-grid">
                <div class="method-card reveal-element">
                    <span class="watermark">01</span>
                    <span class="method-tag">[01_OTIMIZAÇÃO]</span>
                    <i data-lucide="zap" class="w-8 h-8 text-[#888] icon-reveal block mb-4"></i>
                    <h3 class="text-2xl font-display font-bold text-[#f0f0f0] mb-2">Otimização Inteligente</h3>
                    <p class="text-[#888888] font-light">Mapeamento estratégico de gargalos e estruturação de fluxos de trabalho autônomos.</p>
                </div>
                
                <div class="method-card reveal-element" style="transition-delay: 0.1s;">
                    <span class="watermark">02</span>
                    <span class="method-tag">[02_AUTOMAÇÃO]</span>
                    <i data-lucide="file-code" class="w-8 h-8 text-[#888] icon-reveal block mb-4"></i>
                    <h3 class="text-2xl font-display font-bold text-[#f0f0f0] mb-2">Automação de Docs</h3>
                    <p class="text-[#888888] font-light">Engenharia de Prompt para redigir documentos técnicos e relatórios perfeitamente alinhados.</p>
                </div>

                <div class="method-card reveal-element" style="transition-delay: 0.2s;">
                    <span class="watermark">03</span>
                    <span class="method-tag">[03_AUDITORIA]</span>
                    <i data-lucide="shield-check" class="w-8 h-8 text-[#888] icon-reveal block mb-4"></i>
                    <h3 class="text-2xl font-display font-bold text-[#f0f0f0] mb-2">Auditoria de IA</h3>
                    <p class="text-[#888888] font-light">Segurança absoluta com RLHF e LLM Alignment auditado pelo humano para eliminar alucinações.</p>
                </div>

                <div class="method-card reveal-element" style="transition-delay: 0.3s;">
                    <span class="watermark">04</span>
                    <span class="method-tag">[04_PRECISÃO]</span>
                    <i data-lucide="target" class="w-8 h-8 text-[#ff2a2a] icon-reveal block mb-4"></i>
                    <h3 class="text-2xl font-display font-bold text-[#f0f0f0] mb-2">Precisão Garantida</h3>
                    <p class="text-[#888888] font-light">Nossos fluxos revisam a si mesmos, garantindo 100% de confiabilidade técnica nas entregas.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Seção Especialista -->
    <section id="mentor" class="relative z-20 bg-[#0d0d0d] border-t border-[rgba(255,42,42,0.12)]">
        <div class="grid grid-cols-1 lg:grid-cols-2 w-full max-w-[1400px] mx-auto px-6 lg:px-12 py-24 gap-16">
            <div class="reveal-element">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-sm border border-[rgba(255,42,42,0.3)] bg-[#111] mb-6">
                    <span class="text-xs font-medium tracking-wide text-[#ff2a2a] uppercase font-tech pl-1">O Especialista</span>
                </div>
                <h2 class="text-5xl lg:text-8xl font-black font-display tracking-tighter text-[#f0f0f0] leading-[0.9] uppercase mb-4">
                    VITALINO.
                </h2>
                <p class="text-[#888] text-xl font-light mb-12 italic border-l-2 border-[#ff2a2a] pl-4">
                    Especialista em Avaliação de IA e Engenharia de Prompt
                </p>

                <!-- Profile Card + Img -->
                <div id="mentor-img-wrapper" class="relative w-full aspect-[3/4] max-w-sm bg-[#111] border border-[rgba(255,42,42,0.2)] rounded-sm overflow-hidden" style="cursor: pointer;">
                    <img id="mentor-img" src="./assets/mentor.jpg" alt="Vitalino" class="w-full h-full object-cover object-top absolute inset-0 mix-blend-luminosity">
                    <div class="scanline"></div>
                    <div class="scanner-line"></div>
                    <div class="auth-key-tag font-tech text-xs tracking-widest">[AUTH_KEY VERIFIED]</div>
                </div>
            </div>

            <div class="flex flex-col justify-center reveal-element" style="transition-delay: 0.2s;">
                <p class="text-2xl font-light text-[#f0f0f0] mb-12 italic leading-relaxed">
                    "Minha especialidade é capturar a inteligência do seu negócio e transformá-la em fluxos automatizados. Combinando Neurociência com o desenvolvimento de fluxos recursivos, garanto que a IA atue a seu favor com precisão cirúrgica."
                </p>

                <div class="grid grid-cols-2 gap-6 mb-12">
                    <div class="flex items-center gap-3">
                        <i data-lucide="brain" class="text-[#888] w-5 h-5"></i>
                        <span class="font-tech text-xs uppercase text-[#888]">Neurociências</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <i data-lucide="cpu" class="text-[#888] w-5 h-5"></i>
                        <span class="font-tech text-xs uppercase text-[#888]">IA Generativa</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <i data-lucide="graduation-cap" class="text-[#888] w-5 h-5"></i>
                        <span class="font-tech text-xs uppercase text-[#888]">MBA IA</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <i data-lucide="users" class="text-[#888] w-5 h-5"></i>
                        <span class="font-tech text-xs uppercase text-[#888]">Psicologia</span>
                    </div>
                </div>

                <a href="https://wa.me/5522998586180" target="_blank" class="mt-auto btn-primary inline-flex items-center justify-center gap-2 py-4 px-8 rounded-sm font-tech text-xs uppercase tracking-widest w-fit">
                    Fale comigo <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Depoimentos -->
    <section class="bg-[#080808] py-24 border-t border-[rgba(255,42,42,0.12)]">
        <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
            <h2 class="text-4xl font-display font-black text-[#f0f0f0] uppercase mb-12 reveal-element">Resultados Reais</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Depo 1 -->
                <div class="bg-[#111111] border border-[rgba(255,42,42,0.12)] p-8 rounded-sm reveal-right hover:border-[#ff2a2a] transition-colors">
                    <div class="flex gap-1 text-[#ff2a2a] mb-6">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                    </div>
                    <p class="text-[#888] font-light italic mb-8">"A automação de documentos reduziu em 70% o tempo da minha equipe jurídica. O Vitalino entregou precisão absoluta."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-10 h-10 rounded-full bg-[#ff2a2a] text-[#f0f0f0] font-tech text-xs flex items-center justify-center font-bold">RC</div>
                        <div>
                            <p class="text-[#f0f0f0] font-medium text-sm">Ricardo Costa</p>
                            <p class="text-[#888] text-[10px] font-tech uppercase tracking-widest">Dir. Operações</p>
                        </div>
                    </div>
                </div>
                <!-- Depo 2 -->
                <div class="bg-[#111111] border border-[rgba(255,42,42,0.12)] p-8 rounded-sm reveal-right hover:border-[#ff2a2a] transition-colors" style="transition-delay: 0.15s;">
                    <div class="flex gap-1 text-[#ff2a2a] mb-6">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                    </div>
                    <p class="text-[#888] font-light italic mb-8">"Nossos processos internos eram caos. Com a IA aplicada pelo Vitalino, ganhamos escala em 30 dias."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-10 h-10 rounded-full bg-[#ff2a2a] text-[#f0f0f0] font-tech text-xs flex items-center justify-center font-bold">FL</div>
                        <div>
                            <p class="text-[#f0f0f0] font-medium text-sm">Fernanda Lima</p>
                            <p class="text-[#888] text-[10px] font-tech uppercase tracking-widest">CEO Startup</p>
                        </div>
                    </div>
                </div>
                <!-- Depo 3 -->
                <div class="bg-[#111111] border border-[rgba(255,42,42,0.12)] p-8 rounded-sm reveal-right hover:border-[#ff2a2a] transition-colors" style="transition-delay: 0.3s;">
                    <div class="flex gap-1 text-[#ff2a2a] mb-6">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>
                    </div>
                    <p class="text-[#888] font-light italic mb-8">"Eliminamos 100% das alucinações em nossos relatórios com os fluxos de AI implementados. Impressionante."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-10 h-10 rounded-full bg-[#ff2a2a] text-[#f0f0f0] font-tech text-xs flex items-center justify-center font-bold">MA</div>
                        <div>
                            <p class="text-[#f0f0f0] font-medium text-sm">Marcelo Andrade</p>
                            <p class="text-[#888] text-[10px] font-tech uppercase tracking-widest">Gerente TI</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Final -->
    <section class="relative bg-gradient-to-t from-[rgba(255,42,42,0.05)] to-[#080808] py-32 text-center border-t border-[rgba(255,42,42,0.12)]">
        <div class="absolute inset-0 z-0 bg-transparent flex justify-center items-center pointer-events-none">
             <div class="w-[800px] h-[500px] rounded-full bg-[#ff2a2a] opacity-[0.03] blur-[150px]"></div>
        </div>
        <div class="relative z-10 reveal-element">
            <!-- Decorative line -->
            <div class="w-16 h-1 bg-[#ff2a2a] mx-auto mb-8 rounded-full shadow-[0_0_10px_#ff2a2a]"></div>
            <h2 class="text-5xl md:text-7xl font-display font-black text-[#f0f0f0] mb-8 uppercase tracking-tighter">Eleve Sua Operação</h2>
            <p class="text-[#888] text-xl font-light mb-12 max-w-2xl mx-auto">Pronto para trazer automação estruturada e segurança absoluta para a sua operação?</p>
            <a href="https://wa.me/5522998586180?text=Olá%20Vitalino,%20gostaria%20de%20agendar%20um%20diagnóstico%20de%20processos" target="_blank" class="btn-primary inline-flex items-center gap-3 px-10 py-5 rounded-sm font-tech font-bold uppercase tracking-widest text-sm shadow-[0_0_20px_rgba(255,42,42,0.2)] group relative overflow-hidden">
                <span class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform"></span>
                <i data-lucide="message-circle" class="w-5 h-5 relative z-10"></i>
                <span class="relative z-10">FALAR VIA WHATSAPP</span>
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-[#050505] border-t border-[rgba(255,42,42,0.15)] py-12">
        <div class="max-w-[1400px] mx-auto px-6 lg:px-12 grid grid-cols-1 md:grid-cols-4 gap-8 reveal-element">
            <div>
                <h3 class="text-2xl font-display font-black text-[#f0f0f0] mb-4 text-glow-red uppercase">VITALINO<span class="text-[#ff2a2a]">.</span></h3>
                <p class="text-[#888] text-sm">Engenharia de Conhecimento e IA.</p>
            </div>
            <div>
                <h4 class="text-[#f0f0f0] font-tech text-xs uppercase mb-4 tracking-widest">Contato</h4>
                <div class="flex flex-col gap-3 text-sm text-[#888]">
                    <span class="flex items-center gap-2 hover:text-[#ff2a2a] cursor-pointer transition-colors"><i data-lucide="mail" class="w-4 h-4"></i> contato@vitalino.com.br</span>
                    <span class="flex items-center gap-2 hover:text-[#ff2a2a] cursor-pointer transition-colors"><i data-lucide="map-pin" class="w-4 h-4"></i> Brasil</span>
                    <span class="flex items-center gap-2 hover:text-[#ff2a2a] cursor-pointer transition-colors"><i data-lucide="message-circle" class="w-4 h-4"></i> WhatsApp Exclusivo</span>
                </div>
            </div>
            <div>
                <h4 class="text-[#f0f0f0] font-tech text-xs uppercase mb-4 tracking-widest">Legal</h4>
                <div class="flex flex-col gap-3 text-sm text-[#888]">
                    <a href="#" class="hover:text-[#f0f0f0] transition-colors">Termos de Uso</a>
                    <a href="#" class="hover:text-[#f0f0f0] transition-colors">Privacidade</a>
                </div>
            </div>
            <div class="text-right">
                <p class="text-[10px] text-[#888] font-tech mt-8 uppercase tracking-widest border-t border-[#1a1a1a] pt-4">© 2025 Vitalino. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Logic Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            lucide.createIcons(); // Initialize all lucide icons

            // PRELOADER DOOR EFFECT (Split Reveal): remove after 1.8s
            const preloader = document.getElementById('preloader');
            const dLeft = document.getElementById('door-left');
            const dRight = document.getElementById('door-right');
            const preContent = document.getElementById('preloader-content');

            // Force preloader to top of zindex on mobile
            document.body.style.overflow = 'hidden';

            setTimeout(() => {
                dLeft.classList.add('door-open-left');
                dRight.classList.add('door-open-right');
                preContent.classList.add('opacity-0');
                
                setTimeout(() => {
                    preloader.remove(); 
                    document.body.style.overflow = '';
                }, 900); // Wait for transition
                
            }, 1000); // 1 second boot screen

            // GLOBAL SCROLL REVEAL (Intersection Observer)
            const revealOptions = { rootMargin: '0px 0px -50px 0px', threshold: 0.15 };
            const revealObserver = new IntersectionObserver((entries, obs) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        obs.unobserve(entry.target);
                        // Trigger inner icon reveal
                        entry.target.querySelectorAll('.icon-reveal').forEach(ic => ic.classList.add('is-visible'));
                    }
                });
            }, revealOptions);

            document.querySelectorAll('.reveal-element, .reveal-right').forEach(el => revealObserver.observe(el));

            // METHOD PROGRESS LINE
            const methodSection = document.getElementById('method');
            const progressLine = document.querySelector('.method-progress-line');
            if (methodSection && progressLine) {
                window.addEventListener('scroll', () => {
                    const rect = methodSection.getBoundingClientRect();
                    const winH = window.innerHeight;
                    if(rect.top < winH && rect.bottom > 0) {
                        let pct = ((winH - rect.top) / (rect.height + winH/2)) * 100;
                        pct = Math.max(0, Math.min(100, pct));
                        progressLine.style.height = pct + '%';
                    }
                }, {passive:true});
            }

            // PARALLAX ESPECIALISTA
            const imgWrapper = document.getElementById('mentor-img-wrapper');
            const img = document.getElementById('mentor-img');
            if(imgWrapper && img) {
                imgWrapper.addEventListener('mousemove', (e) => {
                    const rect = imgWrapper.getBoundingClientRect();
                    const xPos = (e.clientX - rect.left) / rect.width;
                    const yPos = (e.clientY - rect.top) / rect.height;
                    const moveX = (xPos - 0.5) * 10; // -5 to +5
                    const moveY = (yPos - 0.5) * 10;
                    img.style.transform = `translate(${moveX}px, ${moveY}px) scale(1.05)`;
                });
                imgWrapper.addEventListener('mouseleave', () => {
                    img.style.transform = 'translate(0px, 0px) scale(1)';
                });
            }

        });
    </script>
</body>
</html>
