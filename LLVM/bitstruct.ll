; ModuleID = 'bitstruct.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.anon = type <{ i8, i16, float, i16, i8 }>

@Packet = common global %struct.anon zeroinitializer, align 1

; Function Attrs: nounwind uwtable
define void @encode() #0 {
  store i8 1, i8* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 0), align 1
  store i16 2, i16* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 1), align 1
  store float 3.000000e+00, float* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 2), align 1
  %1 = load i16, i16* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 3), align 1
  %2 = and i16 %1, -1017
  %3 = or i16 %2, 32
  store i16 %3, i16* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 3), align 1
  %4 = load i16, i16* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 3), align 1
  %5 = and i16 %4, -1017
  %6 = or i16 %5, 984
  store i16 %6, i16* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 3), align 1
  store i8 1, i8* getelementptr inbounds (%struct.anon, %struct.anon* @Packet, i32 0, i32 4), align 1
  ret void
}

attributes #0 = { nounwind uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.1-24 (tags/RELEASE_381/final)"}
