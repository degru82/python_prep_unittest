import os


filelist = os.listdir('.')
unit_testcase_files = []
for f in filelist:
    if 'testcase_unit__' in f:
        unit_testcase_files.append(f)

for f in unit_testcase_files:
    mod_name = f.split('__')[1]
    mod_testcase_name = 'testcase_mod__' + mod_name + '.txt'
    with open(mod_testcase_name, 'a') as mod_f:
        buf = ''
        with open(f, 'r') as unit_f:
            buf += unit_f.read(100000)
        mod_f.write(buf)
