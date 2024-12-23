import heapq
from collections import defaultdict, Counter

# Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char  # character
        self.freq = freq  # frequency of the character
        self.left = None  # left child
        self.right = None  # right child

    # Define the comparison operators for heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman Tree
def build_huffman_tree(text):
    # Count frequency of each character in the text
    freq = Counter(text)
    
    # Create a priority queue to hold the nodes
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    
    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Generate Huffman codes from the tree
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes

# Encode the text
def huffman_encode(text, codes):
    return ''.join([codes[char] for char in text])

# Decode the encoded text
def huffman_decode(encoded_text, root):
    decoded_text = []
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.char:
            decoded_text.append(current.char)
            current = root
    return ''.join(decoded_text)

# Main function to perform Huffman coding
def huffman_coding(text):
    # Step 1: Build Huffman Tree
    root = build_huffman_tree(text)
    
    # Step 2: Generate Huffman codes
    codes = generate_codes(root)
    
    # Step 3: Encode the text
    encoded_text = huffman_encode(text, codes)
    
    # Step 4: Decode the encoded text to verify correctness
    decoded_text = huffman_decode(encoded_text, root)
    
    return codes, encoded_text, decoded_text

# Example usage
text = input("Enter the Text : ")
codes, encoded_text, decoded_text = huffman_coding(text)

print("Huffman Codes:", codes)
print("Encoded Text:", encoded_text)
print("Decoded Text:", decoded_text)
