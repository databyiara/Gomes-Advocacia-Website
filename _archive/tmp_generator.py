import os
import glob
import re

base_dir = r"c:\Users\iaraf\OneDrive\Desktop\gomes_advocacia"
index3_path = os.path.join(base_dir, "index3.html")
index4_path = os.path.join(base_dir, "index4.html")

with open(index3_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_gsap_update = """                            onUpdate: (self) => {
                                if (scrollyVideo) scrollyVideo.setTargetTimePercent(self.progress);
                            }"""
new_gsap_update = """                            onUpdate: (self) => {
                                // Limita o progresso a 99.9% para evitar congelamento do vídeo
                                let progress = self.progress;
                                if (progress >= 1) progress = 0.999;
                                if (scrollyVideo) scrollyVideo.setTargetTimePercent(progress);
                            }"""
html = html.replace(old_gsap_update, new_gsap_update)

styles_to_inject = """
        /* === NEW AETHER INSPIRED STYLES === */
        
        .karaoke-word {
            transition: opacity 0.3s ease, color 0.3s ease;
        }

        /* Bento cards */
        .bento-card {
            background: linear-gradient(135deg, rgba(20, 20, 20, 0.6) 0%, rgba(8, 8, 8, 0.9) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .bento-card:hover {
            border-color: rgba(16, 185, 129, 0.3);
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.7), 0 0 20px rgba(16, 185, 129, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }

        .bento-spot {
            position: absolute;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.15) 0%, transparent 70%);
            width: 300px;
            height: 300px;
            border-radius: 50%;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.5s ease;
            z-index: 0;
            transform: translate(-50%, -50%);
        }

        .bento-card:hover .bento-spot {
            opacity: 1;
        }

        .bento-card > * {
            position: relative;
            z-index: 10;
        }

        /* Timeline Styles */
        .timeline-point {
            box-shadow: 0 0 0 4px #020202, 0 0 0 5px rgba(255,255,255,0.1);
            transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
        }

        .timeline-step-active .timeline-point {
            background-color: #10B981;
            border-color: transparent;
            box-shadow: 0 0 0 4px #020202, 0 0 0 5px rgba(16,185,129,0.3), 0 0 30px rgba(16,185,129,0.6);
            transform: scale(1.2);
        }

        .timeline-step-active .timeline-card-visual {
            border-color: rgba(16,185,129,0.3);
            box-shadow: 0 10px 40px -10px rgba(16,185,129,0.15);
        }

        .timeline-step-active .timeline-text-shard {
            color: #10B981;
            text-shadow: 0 0 10px rgba(16,185,129,0.4);
        }

        @keyframes scan-line {
            0% { transform: translateY(-100%); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(400%); opacity: 0; }
        }

        .timeline-scan-beam {
            background: linear-gradient(180deg, transparent, rgba(16, 185, 129, 0.2), transparent);
            animation: scan-line 3s linear infinite;
        }

        .dark-section-bg {
            background-color: #020202;
            position: relative;
            z-index: 20;
        }
"""

html = html.replace('</style>', styles_to_inject + '\n    </style>')

html_to_inject = """
    <!-- =========================================================
         NEW AETHER INSPIRED SECTIONS
    ========================================================= -->
    <div class="dark-section-bg">
        <!-- Text Section (Karaoke) -->
        <section class="py-40 px-6">
            <div class="max-w-4xl mx-auto text-center">
                <h2 class="text-3xl md:text-[3.5rem] font-semibold leading-[1.3] text-left text-white tracking-tight" id="karaoke-text">
                    <span class="karaoke-word opacity-20">Não</span>
                    <span class="karaoke-word opacity-20">deixe</span>
                    <span class="karaoke-word opacity-20">a</span>
                    <span class="karaoke-word opacity-20">burocracia</span>
                    <span class="karaoke-word opacity-20">travar</span>
                    <span class="karaoke-word opacity-20">o</span>
                    <span class="karaoke-word opacity-20">seu</span>
                    <span class="karaoke-word opacity-20">direito.</span>
                    <span class="karaoke-word opacity-20">O</span>
                    <span class="karaoke-word opacity-20">nosso</span>
                    <span class="karaoke-word opacity-20">sistema</span>
                    <span class="karaoke-word opacity-20">inteligente</span>
                    <span class="karaoke-word opacity-20">acelera</span>
                    <span class="karaoke-word opacity-20">a</span>
                    <span class="karaoke-word opacity-20">análise</span>
                    <span class="karaoke-word opacity-20">e</span>
                    <span class="karaoke-word opacity-20">entrega</span>
                    <span class="karaoke-word opacity-20">resultados</span>
                    <span class="karaoke-word opacity-20">seguros.</span>
                </h2>
            </div>
        </section>

        <!-- Glass Bento Capabilities -->
        <section class="py-32 px-6" id="bento">
            <div class="max-w-6xl mx-auto">
                <div class="text-center mb-14 gsap-fade-up">
                    <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-[#10B981] mb-4">
                        Diferenciais
                    </p>
                    <h2 class="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-4">
                        A plataforma do seu benefício
                    </h2>
                    <p class="text-neutral-400 max-w-xl mx-auto font-light">
                        Estrutura desenhada para conferir máxima transparência, velocidade e excelência ao longo de todo o seu processo previdenciário.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-12 gap-5">
                    <!-- Card 1 -->
                    <article class="bento-card md:col-span-7 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Processamento Inteligente</h3>
                        <p class="text-neutral-400 text-sm max-w-md font-light">
                            Algoritmos de verificação prévia garantem que seus documentos estejam perfeitamente alinhados antes de qualquer petição, poupando meses de espera.
                        </p>
                        <div class="mt-6 flex items-center gap-3 text-xs text-white/70">
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Precisão Absoluta</span>
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Agilidade</span>
                        </div>
                        <img alt="Realtime Sync Visual" class="mt-8 h-48 w-full object-cover rounded-xl border border-white/10 opacity-80 pointer-events-none select-none" src="assets/images/law_office_abstract_" />
                    </article>

                    <!-- Card 2 -->
                    <article class="bento-card md:col-span-5 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Análise de Ponta</h3>
                        <p class="text-neutral-400 text-sm font-light">
                            Trilhas de auditoria garantem a máxima integridade na revisão de seu benefício.
                        </p>
                        <div class="mt-8 grid grid-cols-2 gap-4">
                            <div class="rounded-xl border border-white/10 bg-white/5 p-4">
                                <p class="text-white text-sm font-semibold">100%</p>
                                <p class="text-white/50 text-xs mt-1">Transparência</p>
                            </div>
                            <div class="rounded-xl border border-white/10 bg-white/5 p-4">
                                <p class="text-white text-sm font-semibold">24/7</p>
                                <p class="text-white/50 text-xs mt-1">Acesso ao status</p>
                            </div>
                        </div>
                    </article>

                    <!-- Card 3 -->
                    <article class="bento-card md:col-span-5 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Estratégia Legal</h3>
                        <p class="text-neutral-400 text-sm font-light">
                            Definimos a rota legal exata para aposentadorias seguras e sem revisões surpresa.
                        </p>
                        <img alt="Policy Engine Visual" class="mt-8 h-40 w-full object-cover rounded-xl border border-white/10 opacity-80 pointer-events-none select-none" src="assets/images/legal_documents_glow_" />
                    </article>

                    <!-- Card 4 -->
                    <article class="bento-card md:col-span-7 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Painel de Acompanhamento</h3>
                        <p class="text-neutral-400 text-sm max-w-md font-light">
                            Navegue em tempo real por um painel exclusivo que detalha cada etapa processual do seu requerimento.
                        </p>
                        <div class="mt-7 flex flex-wrap gap-3 text-xs text-white/70">
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Cloud Segura</span>
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Notificações</span>
                        </div>
                        <img alt="Edge Routing Visual" class="mt-8 h-40 w-full object-cover rounded-xl border border-white/10 opacity-80 pointer-events-none select-none" src="assets/images/legal_tech_dashboard_" />
                    </article>
                </div>
            </div>
        </section>

        <!-- Timeline Section -->
        <section class="py-40 px-6 relative overflow-hidden" id="timeline">
            <!-- Ambient Background -->
            <div class="absolute inset-0 pointer-events-none" style="background-image: radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.03) 1px, transparent 1px); background-size: 40px 40px; mask-image: linear-gradient(to bottom, transparent, black 15%, black 85%, transparent);"></div>
            
            <div class="max-w-6xl mx-auto relative z-10">
                <!-- Section Header -->
                <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-8 mb-24 gsap-fade-up">
                    <div>
                        <div class="flex items-center gap-3 mb-4">
                            <div class="h-px w-8 bg-[#10B981]"></div>
                            <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-[#10B981]/90">
                                Fluxo Processual
                            </p>
                        </div>
                        <h2 class="text-3xl md:text-5xl font-semibold tracking-tight text-white leading-tight">
                            Arquitetura de
                            <br/>
                            <span class="text-white/30">
                                Resultados Reais
                            </span>
                        </h2>
                    </div>
                    <p class="text-neutral-400 max-w-sm text-sm leading-relaxed border-l border-white/10 pl-6 font-light">
                        Entenda o protocolo dinâmico de nossa equipe técnica para sintetizar soluções ágeis na concessão de benefícios previdenciários.
                    </p>
                </div>

                <!-- Timeline Track -->
                <div class="relative pl-6 md:pl-0" id="timeline-track">
                    <!-- Central Guide Lines -->
                    <div class="absolute left-6 md:left-1/2 top-0 bottom-0 w-px bg-white/5 md:-translate-x-px"></div>
                    
                    <!-- Active Filling Line -->
                    <div class="absolute left-6 md:left-1/2 top-0 w-px bg-[#10B981] shadow-[0_0_15px_rgba(16,185,129,0.5)] md:-translate-x-px h-0 origin-top z-10" id="timeline-fill">
                        <!-- Scanner Head -->
                        <div class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 w-3 h-3 bg-white rounded-full shadow-[0_0_20px_2px_rgba(16,185,129,0.9)] z-20"></div>
                        <div class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 w-12 h-12 border border-[#10B981]/30 rounded-full animate-[ping_1.5s_cubic-bezier(0,0,0.2,1)_infinite] opacity-50"></div>
                    </div>

                    <!-- Steps Container -->
                    <div class="space-y-32 py-12">
                        <!-- STEP 1 -->
                        <div class="timeline-step relative grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-24 opacity-20 blur-[4px] scale-[0.98] transition-all duration-700 ease-out will-change-transform">
                            <!-- Left: Content -->
                            <div class="md:text-right md:pr-12 relative order-2 md:order-1">
                                <div class="inline-block relative">
                                    <h3 class="text-2xl font-semibold text-white mb-2 tracking-tight">
                                        Análise Tributária & Documental
                                    </h3>
                                    <p class="timeline-text-shard text-[#10B981]/60 text-[10px] font-mono mb-4 uppercase tracking-widest transition-colors duration-500">
                                        EXTRACTION_CNIS // FASE 01
                                    </p>
                                    <p class="text-neutral-400 text-sm leading-relaxed max-w-sm ml-auto font-light">
                                        Aferição automatizada de vínculos e contribuições. Descartamos inconsistências ainda na raiz, preparando o alicerce irrefutável do processo.
                                    </p>
                                </div>
                            </div>
                            <!-- Center Anchor -->
                            <div class="absolute left-6 md:left-1/2 top-0 w-3 h-3 -ml-1.5 rounded-full border border-white/20 bg-[#020202] z-20 timeline-point md:top-6"></div>
                            <!-- Right: Visual -->
                            <div class="pl-12 md:pl-0 order-3 md:order-2">
                                <div class="timeline-card-visual h-32 w-full md:w-72 bg-white/[0.02] rounded-xl border border-white/10 backdrop-blur-md relative overflow-hidden group transition-all duration-500">
                                    <div class="timeline-scan-beam absolute inset-0 w-full h-[50%]"></div>
                                    <div class="absolute inset-0 flex items-center justify-center gap-2">
                                        <div class="w-12 h-12 rounded-lg border border-white/10 flex items-center justify-center bg-black/20">
                                            <div class="w-1 h-1 bg-white/40 rounded-full"></div>
                                        </div>
                                        <div class="w-12 h-12 rounded-lg border border-[#10B981]/20 flex items-center justify-center bg-[#10B981]/5 shadow-[0_0_15px_-5px_rgba(16,185,129,0.3)]">
                                            <div class="w-1.5 h-1.5 bg-[#10B981] rounded-full animate-pulse"></div>
                                        </div>
                                        <div class="w-12 h-12 rounded-lg border border-white/10 flex items-center justify-center bg-black/20">
                                            <div class="w-1 h-1 bg-white/40 rounded-full"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- STEP 2 -->
                        <div class="timeline-step relative grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-24 opacity-20 blur-[4px] scale-[0.98] transition-all duration-700 ease-out will-change-transform">
                            <!-- Left: Visual -->
                            <div class="md:text-right md:pr-0 relative order-3 md:order-1 flex md:justify-end">
                                <div class="pl-12 md:pl-0 md:pr-12 w-full md:w-auto flex justify-end">
                                    <div class="timeline-card-visual h-32 w-full md:w-72 bg-white/[0.02] rounded-xl border border-white/10 backdrop-blur-md relative overflow-hidden flex items-center justify-center transition-all duration-500">
                                        <div class="flex gap-[3px] items-end h-12">
                                            <span class="w-1 bg-[#10B981]/30 rounded-sm animate-[pulse_2s_ease-in-out_infinite]" style="height: 40%"></span>
                                            <span class="w-1 bg-[#10B981]/60 rounded-sm animate-[pulse_2s_ease-in-out_infinite]" style="height: 80%; animation-delay: 0.1s"></span>
                                            <span class="w-1 bg-[#10B981]/40 rounded-sm animate-[pulse_2s_ease-in-out_infinite]" style="height: 60%; animation-delay: 0.2s"></span>
                                            <span class="w-1 bg-[#10B981]/80 rounded-sm animate-[pulse_2s_ease-in-out_infinite]" style="height: 100%; animation-delay: 0.3s"></span>
                                            <span class="w-1 bg-[#10B981]/50 rounded-sm animate-[pulse_2s_ease-in-out_infinite]" style="height: 50%; animation-delay: 0.4s"></span>
                                        </div>
                                        <div class="absolute top-3 right-3 text-[9px] font-mono text-white/20">
                                            JURIS_CALC
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Center Anchor -->
                            <div class="absolute left-6 md:left-1/2 top-0 w-3 h-3 -ml-1.5 rounded-full border border-white/20 bg-[#020202] z-20 timeline-point md:top-6"></div>
                            <!-- Right: Content -->
                            <div class="pl-12 md:pl-0 order-2 md:order-2">
                                <div class="inline-block relative">
                                    <h3 class="text-2xl font-semibold text-white mb-2 tracking-tight">
                                        Arquitetura Jurídica
                                    </h3>
                                    <p class="timeline-text-shard text-[#10B981]/60 text-[10px] font-mono mb-4 uppercase tracking-widest transition-colors duration-500">
                                        PETITION_MOUNT // FASE 02
                                    </p>
                                    <p class="text-neutral-400 text-sm leading-relaxed max-w-sm font-light">
                                        Defesa estratégica. Base jurisprudencial avançada aplicada em tempo real sobre seu cenário contributivo. Garantimos a precisão antes do ajuizamento.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- STEP 3 -->
                        <div class="timeline-step relative grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-24 opacity-20 blur-[4px] scale-[0.98] transition-all duration-700 ease-out will-change-transform">
                            <!-- Left: Content -->
                            <div class="md:text-right md:pr-12 relative order-2 md:order-1">
                                <div class="inline-block relative">
                                    <h3 class="text-2xl font-semibold text-white mb-2 tracking-tight">
                                        Protocolo & Deferimento
                                    </h3>
                                    <p class="timeline-text-shard text-[#10B981]/60 text-[10px] font-mono mb-4 uppercase tracking-widest transition-colors duration-500">
                                        SUCCESS_SYNTHESIS // FASE 03
                                    </p>
                                    <p class="text-neutral-400 text-sm leading-relaxed max-w-sm ml-auto font-light">
                                        Transmissão e sustentação inabalável nos tribunais. O percurso processual é encapsulado em nosso dashboard para seu monitoramento contínuo até a vitória final.
                                    </p>
                                </div>
                            </div>
                            <!-- Center Anchor -->
                            <div class="absolute left-6 md:left-1/2 top-0 w-3 h-3 -ml-1.5 rounded-full border border-white/20 bg-[#020202] z-20 timeline-point md:top-6"></div>
                            <!-- Right: Visual -->
                            <div class="pl-12 md:pl-0 order-3 md:order-2">
                                <div class="w-12 h-12 rounded-full border-2 border-[#10B981] flex items-center justify-center bg-[#10B981]/10 shadow-[0_0_30px_rgba(16,185,129,0.4)]">
                                    <svg class="w-5 h-5 text-[#10B981]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>
    </div>
"""

html = html.replace('<!-- Scripts -->', html_to_inject + '\n    <!-- Scripts -->')

js_to_inject = """
            // 4. Karaoke Effect
            const karaokeWords = document.querySelectorAll('.karaoke-word');
            if (karaokeWords.length > 0) {
                gsap.to(karaokeWords, {
                    opacity: 1,
                    stagger: 0.1,
                    scrollTrigger: {
                        trigger: '#karaoke-text',
                        start: 'top 80%',
                        end: 'bottom 40%',
                        scrub: 1
                    }
                });
            }

            // 5. Bento Spot Hover Effect
            const bentoCards = document.querySelectorAll('.bento-card');
            bentoCards.forEach(card => {
                const spot = card.querySelector('.bento-spot');
                if (spot) {
                    card.addEventListener('mousemove', (e) => {
                        const rect = card.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        spot.style.left = `${x}px`;
                        spot.style.top = `${y}px`;
                    });
                }
            });

            // 6. Timeline Fill Line
            const timelineTrack = document.getElementById('timeline-track');
            const timelineFill = document.getElementById('timeline-fill');
            const timelineSteps = document.querySelectorAll('.timeline-step');

            if (timelineTrack && timelineFill) {
                gsap.to(timelineFill, {
                    height: "100%",
                    ease: "none",
                    scrollTrigger: {
                        trigger: timelineTrack,
                        start: "top center",
                        end: "bottom center",
                        scrub: true,
                        onUpdate: (self) => {
                            const progress = self.progress;
                            
                            timelineSteps.forEach((step, index) => {
                                const stepProgress = (index + 0.15) / timelineSteps.length; 
                                
                                if (progress >= stepProgress) {
                                    if (!step.classList.contains('timeline-step-active')) {
                                        step.classList.add('timeline-step-active');
                                        gsap.to(step, {
                                            opacity: 1,
                                            filter: "blur(0px)",
                                            scale: 1,
                                            duration: 0.6,
                                            ease: "back.out(1.5)"
                                        });
                                    }
                                } else {
                                    if (step.classList.contains('timeline-step-active')) {
                                        step.classList.remove('timeline-step-active');
                                        gsap.to(step, {
                                            opacity: 0.2,
                                            filter: "blur(4px)",
                                            scale: 0.98,
                                            duration: 0.6,
                                            ease: "power2.out"
                                        });
                                    }
                                }
                            });
                        }
                    }
                });
            }
"""

html = html.replace('initScrubbing();\n            }', 'initScrubbing();\n            }\n' + js_to_inject)

images = glob.glob(os.path.join(base_dir, 'assets', 'images', '*.png'))
law_img = 'assets/images/placeholder.png'
doc_img = 'assets/images/placeholder.png'
tech_img = 'assets/images/placeholder.png'

for img in images:
    if 'law_office_abstract' in img:
        law_img = "assets/images/" + os.path.basename(img)
    elif 'legal_documents_glow' in img:
        doc_img = "assets/images/" + os.path.basename(img)
    elif 'legal_tech_dashboard' in img:
        tech_img = "assets/images/" + os.path.basename(img)

html = html.replace("assets/images/law_office_abstract_", law_img)
html = html.replace("assets/images/legal_documents_glow_", doc_img)
html = html.replace("assets/images/legal_tech_dashboard_", tech_img)

with open(index4_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Success')
