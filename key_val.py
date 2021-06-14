def group_by_owners(files):
    val = (list(files.values()))
    val = set(val)
    val = list(val)
    keyst = (list(files.keys()))
    result = {}
    for i in range(len(val)):
        for j in range(len(keyst)):
            if val[i]==list(files.values())[j]:
                dummylist = [keyst[j]]
                if val[i] in result:
                    result[val[i]].append(keyst[j])
                else:
                    result[val[i]] = dummylist
    return result

files = {
'Input.txt': 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy'
}

print(group_by_owners(files))