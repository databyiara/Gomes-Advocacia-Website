import os
import re
import glob
import shutil

# First securely copy images
brain_dir = r"C:\Users\iaraf\.gemini\antigravity\brain\2359f46c-c298-4ff2-b4be-49a90c0f54df"
base_dir = r"c:\Users\iaraf\OneDrive\Desktop\gomes_advocacia"

# copy all new images
images = glob.glob(os.path.join(brain_dir, "*.png"))
for img in images:
    shutil.copy(img, os.path.join(base_dir, 'assets', 'images', os.path.basename(img)))

# Now read index5.html
with open(os.path.join(base_dir, 'index5.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the text Section
karaoke_re = re.compile(
    r'<section class="py-40 px-6">\s*<div class="max-w-4xl mx-auto text-center">.*?id="karaoke-text">.*?</section>',
    re.DOTALL
)

new_karaoke = """<section class="py-40 px-6">
            <div class="max-w-4xl mx-auto text-center">
                <h2 class="text-3xl md:text-[3.5rem] font-semibold leading-[1.3] text-left text-white tracking-tight" id="karaoke-text">
                    <span class="karaoke-word opacity-20">A</span>
                    <span class="karaoke-word opacity-20">nossa</span>
                    <span class="karaoke-word opacity-20">missão</span>
                    <span class="karaoke-word opacity-20">é</span>
                    <span class="karaoke-word opacity-20">lutar</span>
                    <span class="karaoke-word opacity-20">pela</span>
                    <span class="karaoke-word opacity-20">sua</span>
                    <span class="karaoke-word opacity-20">dignidade.</span>
                    <span class="karaoke-word opacity-20">Enxergamos</span>
                    <span class="karaoke-word opacity-20">a</span>
                    <span class="karaoke-word opacity-20">sua</span>
                    <span class="karaoke-word opacity-20">história</span>
                    <span class="karaoke-word opacity-20">de</span>
                    <span class="karaoke-word opacity-20">vida</span>
                    <span class="karaoke-word opacity-20">e</span>
                    <span class="karaoke-word opacity-20">não</span>
                    <span class="karaoke-word opacity-20">abrimos</span>
                    <span class="karaoke-word opacity-20">mão</span>
                    <span class="karaoke-word opacity-20">da</span>
                    <span class="karaoke-word opacity-20">justiça</span>
                    <span class="karaoke-word opacity-20">verdadeira.</span>
                </h2>
            </div>
        </section>"""

html = karaoke_re.sub(new_karaoke, html)

# Find the lawyer image
lawyer_img = 'assets/images/placeholder.png'
law_images = glob.glob(os.path.join(base_dir, 'assets', 'images', '*.png'))
for i in law_images:
    if 'lawyer_portrait' in i:
        lawyer_img = "assets/images/" + os.path.basename(i)

# Replace the Bento section
bento_re = re.compile(
    r'<section class="py-32 px-6" id="bento">.*?</section>',
    re.DOTALL
)

new_bento = f"""<section class="py-32 px-6" id="bento">
            <div class="max-w-6xl mx-auto">
                <div class="text-center mb-14 gsap-fade-up">
                    <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-[#10B981] mb-4">
                        Nossos Diferenciais
                    </p>
                    <h2 class="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-4">
                        Uma advocacia de excelência e humanidade
                    </h2>
                    <p class="text-neutral-400 max-w-xl mx-auto font-light">
                        Ao nos contratar, você conta com um escritório altamente capacitado que blindará os seus direitos perante a rigidez do INSS.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-12 gap-5">
                    <!-- Card 1 -->
                    <article class="bento-card md:col-span-7 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Atendimento Altamente Humanizado</h3>
                        <p class="text-neutral-400 text-sm max-w-md font-light">
                            Sabemos que atrás de cada requerimento existe a vida e a dignidade de uma pessoa ou de uma família inteira. Valorizamos a sua história.
                        </p>
                        <div class="mt-6 flex items-center gap-3 text-xs text-white/70">
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Empatia</span>
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Acolhimento</span>
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Dedicação</span>
                        </div>
                    </article>

                    <!-- Card 2 -->
                    <article class="bento-card md:col-span-5 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Dra. Clarice Gomes Neto</h3>
                        <p class="text-neutral-400 text-sm font-light">
                            Especialista máxima. Uma advocacia combativa, detalhista, que não aceita "Nãos" vazios do sistema sem uma robusta base legal em favor da sua vivência.
                        </p>
                        <img alt="Dra Clarice Gomes Neto" class="mt-8 h-48 w-full object-cover rounded-xl border border-white/10 opacity-90 pointer-events-none select-none" src="{lawyer_img}" />
                    </article>

                    <!-- Card 3 -->
                    <article class="bento-card md:col-span-5 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Foco Previdenciário</h3>
                        <p class="text-neutral-400 text-sm font-light">
                            A concentração na Previdência nos confere domínio irrestrito das teses mais novas dos tribunais, buscando aposentadorias robustas.
                        </p>
                        <div class="mt-8 grid grid-cols-2 gap-4">
                            <div class="rounded-xl border border-white/10 bg-white/5 p-4">
                                <p class="text-[#10B981] text-sm font-semibold">Decisões</p>
                                <p class="text-white/50 text-xs mt-1">Impactos imediatos</p>
                            </div>
                            <div class="rounded-xl border border-white/10 bg-white/5 p-4">
                                <p class="text-[#10B981] text-sm font-semibold">Teses</p>
                                <p class="text-white/50 text-xs mt-1">Sempre atualizadas</p>
                            </div>
                        </div>
                    </article>

                    <!-- Card 4 -->
                    <article class="bento-card md:col-span-7 p-7 rounded-[22px] backdrop-blur-xl relative overflow-hidden gsap-fade-up">
                        <div class="bento-spot"></div>
                        <h3 class="text-white font-semibold text-xl mb-2">Honestidade & Transparência</h3>
                        <p class="text-neutral-400 text-sm max-w-md font-light">
                            Mantemos você no controle. Informações cristalinas, repasses de andamento constantes e comunicação sempre disposta sem barreiras corporativas. Não criamos falsas ilusões.
                        </p>
                        <div class="mt-7 flex flex-wrap gap-3 text-xs text-white/70">
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Clareza no Processo</span>
                            <span class="px-3 py-1 rounded-full border border-white/10 bg-white/5">Comunicação Humana</span>
                        </div>
                    </article>
                </div>
            </div>
        </section>"""

html = bento_re.sub(new_bento, html)

with open(os.path.join(base_dir, 'index6.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated perfectly.")
