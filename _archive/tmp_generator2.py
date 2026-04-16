import os
import glob

base_dir = r"c:\Users\iaraf\OneDrive\Desktop\gomes_advocacia"
index5_path = os.path.join(base_dir, "index5.html")

with open(index5_path, 'r', encoding='utf-8') as f:
    html = f.read()

images = glob.glob(os.path.join(base_dir, 'assets', 'images', '*.png'))
gavel_img = 'assets/images/placeholder.png'
const_img = 'assets/images/placeholder.png'
scales_img = 'assets/images/placeholder.png'

for img in images:
    if 'justice_gavel' in img:
        gavel_img = "assets/images/" + os.path.basename(img)
    elif 'constitution_glowing' in img:
        const_img = "assets/images/" + os.path.basename(img)
    elif 'scales_of_justice' in img:
        scales_img = "assets/images/" + os.path.basename(img)

# HTML for the new sections
html_to_inject = f"""

        <!-- Expertises / Services Section -->
        <section class="py-32 px-6 border-t border-white/5 relative overflow-hidden" id="especialidades">
            <!-- Decorative Elements -->
            <div class="absolute right-0 top-0 w-1/3 h-full bg-gradient-to-l from-[#10B981]/5 to-transparent pointer-events-none"></div>
            <div class="max-w-6xl mx-auto relative z-10">
                <div class="flex flex-col md:flex-row gap-16 items-center">
                    <div class="flex-1 gsap-fade-up">
                        <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-[#10B981] mb-4">
                            Áreas de Atuação
                        </p>
                        <h2 class="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-6">
                            Direito<br/>Previdenciário<br/><span class="text-white/30">de Alta Performance</span>
                        </h2>
                        <p class="text-neutral-400 text-sm leading-relaxed mb-8 max-w-md font-light">
                            Não atuamos como generalistas. Nossa equipe respira previdência todos os dias, aplicando tecnologia e teses jurídicas de ponta para reverter negativas do INSS e garantir o teto do seu benefício.
                        </p>
                        
                        <div class="space-y-6">
                            <div class="group flex items-start gap-4">
                                <div class="w-10 h-10 rounded-lg border border-white/10 bg-white/5 flex items-center justify-center group-hover:border-[#10B981]/50 group-hover:bg-[#10B981]/10 transition-colors">
                                    <svg class="w-5 h-5 text-neutral-400 group-hover:text-[#10B981] transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                </div>
                                <div>
                                    <h4 class="text-white font-semibold mb-1">Aposentadoria de Valor Máximo</h4>
                                    <p class="text-neutral-500 text-xs font-light">Especial, por idade, por tempo de contribuição ou regras de transição precisas.</p>
                                </div>
                            </div>

                            <div class="group flex items-start gap-4">
                                <div class="w-10 h-10 rounded-lg border border-white/10 bg-white/5 flex items-center justify-center group-hover:border-[#10B981]/50 group-hover:bg-[#10B981]/10 transition-colors">
                                    <svg class="w-5 h-5 text-neutral-400 group-hover:text-[#10B981] transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                                </div>
                                <div>
                                    <h4 class="text-white font-semibold mb-1">Revisões (Vida Toda & Outras)</h4>
                                    <p class="text-neutral-500 text-xs font-light">Recalculamos seu passado contributivo em busca de teses já aprovadas nos tribunais superiores.</p>
                                </div>
                            </div>

                            <div class="group flex items-start gap-4">
                                <div class="w-10 h-10 rounded-lg border border-white/10 bg-white/5 flex items-center justify-center group-hover:border-[#10B981]/50 group-hover:bg-[#10B981]/10 transition-colors">
                                    <svg class="w-5 h-5 text-neutral-400 group-hover:text-[#10B981] transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 4v16m8-8H4"></path></svg>
                                </div>
                                <div>
                                    <h4 class="text-white font-semibold mb-1">Auxílios e BPC/LOAS</h4>
                                    <p class="text-neutral-500 text-xs font-light">Suporte assertivo em benefícios por incapacidade e assistência social com amparo pericial privado.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex-1 relative gsap-fade-up">
                        <div class="aspect-square rounded-2xl overflow-hidden border border-white/10 shadow-[0_0_50px_rgba(16,185,129,0.15)] relative">
                            <img src="{gavel_img}" alt="Direito Previdenciário" class="w-full h-full object-cover">
                        </div>
                        <!-- Floating Small Image -->
                        <div class="absolute -bottom-10 -left-10 w-48 h-48 rounded-2xl overflow-hidden border border-[#10B981]/30 shadow-[0_0_40px_rgba(0,0,0,0.8)] hidden md:block anim-float">
                            <img src="{const_img}" alt="Leis Previdenciárias" class="w-full h-full object-cover">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Stats Section -->
        <section class="py-20 border-y border-white/5 bg-white/[0.01]">
            <div class="max-w-6xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
                <div class="gsap-fade-up">
                    <div class="text-3xl font-bold text-white mb-1">98.5%</div>
                    <div class="text-xs font-medium uppercase tracking-wider text-neutral-500">Êxito Administrativo</div>
                </div>
                <div class="gsap-fade-up" style="transition-delay:100ms">
                    <div class="text-3xl font-bold text-white mb-1">15k+</div>
                    <div class="text-xs font-medium uppercase tracking-wider text-neutral-500">Benefícios Concedidos</div>
                </div>
                <div class="gsap-fade-up" style="transition-delay:200ms">
                    <div class="text-3xl font-bold text-white mb-1">48h</div>
                    <div class="text-xs font-medium uppercase tracking-wider text-neutral-500">Análise Inicial Média</div>
                </div>
                <div class="gsap-fade-up" style="transition-delay:300ms">
                    <div class="text-3xl font-bold text-white mb-1">20+</div>
                    <div class="text-xs font-medium uppercase tracking-wider text-neutral-500">Anos de Especialização</div>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="py-32 px-6 relative overflow-hidden">
            <div class="absolute inset-0 z-0">
                <img src="{scales_img}" alt="Gomes Advocacia Background" class="w-full h-full object-cover opacity-20 filter blur-sm">
                <div class="absolute inset-0 bg-black/80 bg-gradient-to-t from-[#020202] via-[#020202]/90 to-transparent"></div>
            </div>
            
            <div class="max-w-4xl mx-auto text-center relative z-10 gsap-fade-up">
                <h2 class="text-4xl md:text-6xl font-semibold tracking-tighter text-white mb-6">
                    Aposente-se com <span class="text-gradient-green">Dignidade.</span>
                </h2>
                <p class="text-lg text-neutral-400 mb-10 max-w-2xl mx-auto font-light leading-relaxed">
                    Não aceite a contagem padrão do INSS sem uma revisão especializada. Nós assumimos o seu caso e lutamos pelo reconhecimento integral dos seus direitos.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <button class="btn-primary h-14 px-8 md:px-10 rounded-full text-[14px] uppercase tracking-wider font-semibold flex items-center justify-center gap-3">
                        Agendar Análise Gratuita
                        <iconify-icon icon="solar:arrow-right-linear" class="text-lg"></iconify-icon>
                    </button>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="py-12 border-t border-white/5 bg-[#020202] relative z-20">
            <div class="max-w-6xl mx-auto px-6">
                <div class="flex flex-col md:flex-row justify-between items-center gap-6">
                    <div class="flex flex-col items-center md:items-start">
                        <span class="text-white text-xl drop-shadow-md flex items-baseline gap-[6px] mb-2" style="font-family: 'Playfair Display', serif;">
                            <span class="font-semibold tracking-[0.03em]">Gomes</span>
                            <span class="font-normal italic tracking-widest text-[#10B981]">Advocacia</span>
                        </span>
                        <p class="text-xs text-neutral-500 font-mono">OAB/SP 123.456 - Especialistas no RGPS.</p>
                    </div>
                    
                    <div class="flex gap-6 text-sm text-neutral-400">
                        <a href="#" class="hover:text-white transition-colors">Termos de Uso</a>
                        <a href="#" class="hover:text-white transition-colors">Privacidade</a>
                        <a href="#" class="hover:text-white transition-colors">Contato</a>
                    </div>
                    
                    <div class="text-xs text-neutral-600 font-mono">
                        © 2026 Gomes Advocacia. All rights reserved.
                    </div>
                </div>
            </div>
        </footer>
"""

# We'll inject right before `</section>\n    </div>` around line 980
injection_target = '</section>\n    </div>'
if injection_target in html:
    html = html.replace(injection_target, f'</section>\n{html_to_inject}\n    </div>')
else:
    # Fallback to appending before the Scripts tag
    html = html.replace('<!-- Scripts -->', f'{html_to_inject}\n    <!-- Scripts -->')

with open(index5_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished!")
