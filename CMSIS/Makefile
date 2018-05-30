src: \
	src/startup_stm32f051x8.s src/startup_stm32l073xx.s \
	src/system_stm32f0xx.c src/system_stm32l0xx.c

F0CMSIS = STM32/STM32Cube_FW_F0_V1.9.0/Drivers/CMSIS
L0CMSIS = STM32/STM32Cube_FW_L0_V1.10.0/Drivers/CMSIS
F0TMPL  = $(F0CMSIS)/Device/ST/STM32F0xx/Source/Templates
L0TMPL  = $(L0CMSIS)/Device/ST/STM32L0xx/Source/Templates

src/%.s: $(F0TMPL)/gcc/%.s
	cp $< $@
src/%.s: $(L0TMPL)/gcc/%.s
	cp $< $@

src/%.c: $(F0TMPL)/%.c
	cp $< $@
src/%.c: $(L0TMPL)/%.c
	cp $< $@
