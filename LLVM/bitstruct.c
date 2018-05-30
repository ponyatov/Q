#include <stdint.h>
#include <stdbool.h>

struct __attribute__((packed)) {
	uint8_t 		A;
	__attribute__((scalar_storage_order("big")))
	int16_t 		B;
	float   		C;
	unsigned int	D:3;
	  signed int	E:7;
	  bool			F;
} Packet;

void encode() {
	Packet.A=1; Packet.B=2; 	// integers
	Packet.C=3; 				// float
	Packet.E=4; Packet.E=-5;	// bit field integers
	Packet.F = true;			// boolean
}
