from huffman import HuffmanCoding

#input file path... size: 715.3 kB
path = "/home/ahmed/Desktop/sample.txt"
h = HuffmanCoding(path)

output_path = h.compress()
#compressed file size = 637.0 kB
h.decompress(output_path)