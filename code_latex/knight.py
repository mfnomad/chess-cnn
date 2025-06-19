//leeres Spielfeld
U64 attacks, knights = 0ULL; 

// platziert Springer auf dem Brett
set_bit(knights, square);

// Springer Zuege lassen sich mithilfe von Bit-Shifts generieren
attacks = (((knights >> 6)  | (knights << 10)) & ~FILE_GH) |
          (((knights >> 10) | (knights << 6))  & ~FILE_AB) |
          (((knights >> 15) | (knights << 17)) & ~FILE_H)  |
          (((knights >> 17) | (knights << 15)) & ~FILE_A);
