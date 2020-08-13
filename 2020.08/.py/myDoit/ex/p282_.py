import sys

src = sys.argv[1]

dst = sys.argv[2]

# print(src)
# print(dst)

with open(src) as f:
    data = f.read()

space_content = data.replace('\t', ' '*4)
print(space_content)

with open(dst, 'w') as f:
    f.write(space_content)