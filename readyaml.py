import yaml

data = dict(
    A = 'a',
    B = dict(
        C = 'c',
        D = 'd',
        E = 'e',
    )
)

with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)


rec_file=open('data.yml','r')

rec=yaml.load(rec_file)
print(yaml.dump(rec))



