CFLAGS += -O0 -g -ffunction-sections

LIB += lib/libSTM32.a

OBJ	+= lib/startup_stm32f051x8.o lib/system_stm32f0xx.o

S	+= src/startup_stm32f051x8.s src/startup_stm32l073xx.s
C	+= src/system_stm32f0xx.c 	 src/system_stm32l0xx.c

H	+= include/system_stm32f0xx.h include/system_stm32l0xx.h
H	+= include/stm32f0xx.h		  include/stm32l0xx.h

H	+= include/stm32f051x8.h

H	+= include/core_cm0.h include/cmsis_gcc.h
H	+= include/core_cmInstr.h include/core_cmFunc.h

LDS	+= lib/STM32L073VZTx_FLASH.ld lib/STM32L051R8_FLASH.ld

SRC += $(S) $(C) $(H) $(LDS)

lib: $(LIB)

$(LIB): $(OBJ)

$(OBJ): $(SRC)

clean:
	rm -f lib/*.o lib/*.a

F0CUBE	= STM32/STM32Cube_FW_F0_V1.9.0
L0CUBE	= STM32/STM32Cube_FW_L0_V1.10.0
F0CMSIS = $(F0CUBE)/Drivers/CMSIS/Device/ST/STM32F0xx
L0CMSIS = $(L0CUBE)/Drivers/CMSIS/Device/ST/STM32L0xx
F0TMPL  = $(F0CMSIS)/Source/Templates
L0TMPL  = $(L0CMSIS)/Source/Templates
F0INCL	= $(F0CMSIS)/Include
L0INCL	= $(L0CMSIS)/Include
CMINCL	= STM32/STM32Cube_FW_L0_V1.10.0/Drivers/CMSIS/Include
L0PRJ	= $(L0CUBE)/Projects/STM32L073Z_EVAL/Templates_LL

DISCO	= STM32/STM32F0-Discovery_FW_V1.0.0/Project/Demonstration/TrueSTUDIO/STM32F0-Discovery_Demo

lib/%.ld: $(L0PRJ)/SW4STM32/STM32L073Z_EVAL/%.ld
	cp $< $@
lib/STM32L051R8_FLASH.ld: $(DISCO)/stm32_flash.ld
	cp $< $@

src/%.s: $(F0TMPL)/gcc/%.s
	cp $< $@
src/%.s: $(L0TMPL)/gcc/%.s
	cp $< $@

src/%.c: $(F0TMPL)/%.c
	cp $< $@
src/%.c: $(L0TMPL)/%.c
	cp $< $@
	
include/%.h: $(F0INCL)/%.h
	cp $< $@
include/%.h: $(L0INCL)/%.h
	cp $< $@
include/%.h: $(CMINCL)/%.h
	cp $< $@

CC		= arm-none-eabi-gcc
CFLAGS += -I$(CURDIR)/include

lib/system_stm32f0xx.o: src/system_stm32f0xx.c 
	$(CC) $(CFLAGS) -DSTM32F051x8  -c -o $@ $<
lib/system_stm32l0xx.o: src/system_stm32l0xx.c 
	$(CC) $(CFLAGS) -D STM32L073xx -c -o $@ $<
	
lib/%.o: src/%.c 
	$(CC) $(CFLAGS) -c -o $@ $<
lib/%.o: src/%.s 
	$(CC) $(CFLAGS) -c -o $@ $<
