

class bitarray(object):
    def __init__(self, data='', endian='big'):
        self._data = data
        self._endian = endian

    def __getitem__(self, index):
        if isinstance(index, slice):
            return bitarray(
                self._data.__getitem__(index),
                self._endian)
            return ret
        else:
            return self._data[index] == '1'
    def tobytes(self):
        result = []
        data = self._data
        endian = self._endian
        if endian == 'big':
            if len(data) % 8 != 0:
                data += '0'*(8-len(data)%8)
            bits = []
            for i in range(0, len(data), 8):
                byte = data[i:i+8]+'0'*(8-len(data[i:i+8]))
                bits.extend([{'0':0,'1':1}[b] for b in byte])
        else:
            bits = []
            for i in range(0, len(data), 8):
                byte = data[i:i+8]+'0'*(8-len(data[i:i+8]))
                bits.extend([{'0':0,'1':1}[b] for b in byte[::-1]])

        for i in range(0, len(bits), 8):
            b = bits[i:i+8]
            b = [1]*(8-len(b)) + b
            result.append(chr(
                b[0] << 7 |
                b[1] << 6 |
                b[2] << 5 |
                b[3] << 4 |
                b[4] << 3 |
                b[5] << 2 |
                b[6] << 1 |
                b[7] << 0))

        return ''.join(result)

    def frombytes(self, input):
        endian = {'big':1, 'little':-1}[self._endian]
        for c in input:
            b = ord(c)
            self._data += ''.join([
                str((b & 0b10000000) >> 7),
                str((b & 0b01000000) >> 6),
                str((b & 0b00100000) >> 5),
                str((b & 0b00010000) >> 4),
                str((b & 0b00001000) >> 3),
                str((b & 0b00000100) >> 2),
                str((b & 0b00000010) >> 1),
                str((b & 0b00000001) >> 0)][::endian])