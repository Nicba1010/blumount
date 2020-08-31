class BitReader(object):
    def __init__(self, f):
        self.input = f
        self.accumulator = 0
        self.bit_count = 0
        self.read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _read_bit(self):
        if not self.bit_count:
            a = self.input.read(1)
            if a:
                self.accumulator = ord(a)
            self.bit_count = 8
            self.read = len(a)
        rv = (self.accumulator & (1 << self.bit_count - 1)) >> self.bit_count - 1
        self.bit_count -= 1
        return rv

    def read_bits(self, n):
        v = 0
        while n > 0:
            v = (v << 1) | self._read_bit()
            n -= 1
        return v
