document.addEventListener("DOMContentLoaded", () => {
            // 1. Initialize Lenis Smooth Scroll
            const lenis = new Lenis({
                duration: 1.5,
                easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
                direction: 'vertical',
                gestureDirection: 'vertical',
                smooth: true,
                mouseMultiplier: 1,
                touchMultiplier: 2,
            });

            function raf(time) {
                lenis.raf(time);
                requestAnimationFrame(raf);
            }
            requestAnimationFrame(raf);

            gsap.registerPlugin(ScrollTrigger);

            lenis.on('scroll', ScrollTrigger.update);
            gsap.ticker.add((time) => { lenis.raf(time * 1000); });
            gsap.ticker.lagSmoothing(0);

            // 2. Trigger Entrance Animations
            const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
            tl.fromTo(".gsap-fade", { opacity: 0, scale: 1.05 }, { opacity: 1, scale: 1, duration: 2.5, ease: "power2.out" }, 0.2);
            tl.to(".headline-line", { opacity: 1, y: "0%", duration: 1.2, stagger: 0.2, ease: "power3.out" }, 0.4);
            tl.fromTo(".gsap-fade-up", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 1.5, stagger: 0.15, ease: "power3.out" }, 0.8);

            // Floating cards stagger entrance
            setTimeout(() => {
                gsap.to('.hero-card', {
                    opacity: 1,
                    y: 0,
                    duration: 1.5,
                    stagger: 0.25,
                    ease: "power4.out",
                    startAt: { y: 40 }
                });
            }, 1000);

            // 3. Cinematic ScrollyVideo Configuration
            const scrollyVideoContainer = document.getElementById("parallax-video");

            if (scrollyVideoContainer) {
                const scrollyVideo = new ScrollyVideo({
                    scrollyVideoContainer: scrollyVideoContainer,
                    src: 'assets/raw_files/video_trimmed.mp4',
                    trackScroll: false,
                    cover: true,
                    transitionSpeed: 0
                });

                const initScrubbing = () => {
                    // Timeline linked to scroll progress via Scrub
                    const scrollTl = gsap.timeline({
                        scrollTrigger: {
                            trigger: ".hero-scroll-container",
                            start: "top top",
                            end: "bottom bottom",
                            scrub: 1.2, // Cinematic smoothing
                            onUpdate: (self) => {
                                // Limita o progresso a 99.9% para evitar congelamento do vídeo
                                let progress = self.progress;
                                if (progress >= 1) progress = 0.999;
                                if (scrollyVideo) scrollyVideo.setTargetTimePercent(progress);
                            }
                        }
                    });

                    // Slightly scale video WITHOUT Y-axis translation to prevent elements from getting cut
                    scrollTl.fromTo(".video-container",
                        { scale: 1 },
                        { scale: 1.04, ease: "none" }, 0
                    );

                    // Fade out dark overlays slightly to make the video shine through clearer when scrolling
                    scrollTl.to(".dark-overlay-left, .dark-overlay-mobile",
                        { opacity: 0, ease: "sine.inOut", duration: 0.3 }, 0
                    );

                    // Fade text out using a secondary timeline linked uniquely to the first 25% of scroll
                    gsap.to(".content-to-blur", {
                        y: -80,
                        opacity: 0,
                        filter: "blur(20px)",
                        scrollTrigger: {
                            trigger: ".hero-scroll-container",
                            start: "top top",
                            end: "25% top",
                            scrub: 1,
                        }
                    });
                };

                initScrubbing();
            }

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

        });