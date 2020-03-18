import re
import json


s_line = ''
f = open(r'json.txt', 'a', encoding='utf-8')
ff = open(r'wrongD.txt', 'a', encoding='utf-8')
with open(r'littledemo26.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        if len(line) != 0:
            s_line = s_line + line
        else:
            a = re.findall(
                r'<docid>(.*?)<docid><major_text>(.*?)<major_text><basic_inf>(.*?)<basic_inf>'
                r'<legal_basis>(.*?)<legal_basis>', s_line, re.S)
            s_line = ''
            dict_x = {}
            for m in a:
                if m:
                    judge = ''
                    b = m[1][:-5] + '"'
                    try:
                        judge = json.loads(b)
                    except:
                        pass
                    if judge == '发布日期： 浏览：次':
                        ff.write(m[0].replace('"', '') + '\n')
                        continue
                    try:
                        s_docid = m[0].replace('"', '')
                        dict_x['docid'] = s_docid
                        smajor_text = json.loads(m[1])
                        dict_x['legal_basis'] = json.loads(m[3])
                        dict_x['major_text'] = smajor_text
                    except:
                        ff.write(m[0].replace('"', '') + '\n')
                        continue
                    sbasic_inf = m[2].replace('"', '')
                    sbasic_inf = sbasic_inf[26:]
                    sbasic_inf = '\\n' + sbasic_inf
                    lbasic_inf = sbasic_inf.split(r'\uff1a')
                    big = []
                    for j in range(len(lbasic_inf)):
                        str_i = ''
                        new = lbasic_inf[j].split(r'\n')
                        del new[0]
                        if len(new) == 0:
                            new.append('\t')
                        if j == 0:
                            big.append(new[0])
                        elif j == len(lbasic_inf) - 1:
                            big.append(new[0])
                        else:
                            if len(new) == 2:
                                big.append(new[0])
                                big.append(new[1])
                            else:
                                for index in new[0:-1]:
                                    str_i = str_i + index + '\t'
                                big.append(str_i)
                                big.append(new[-1])
                    # print(len(big))

                    if len(big) % 2 == 1:
                        ff.write(m[0].replace('"', '') + '\n')
                        continue
                    else:
                        best = []
                        for k in range(len(big)):
                            best.append(big[k].encode('utf-8').decode('unicode_escape'))
                        for l in range(len(best)):
                            if l % 2 == 0:
                                dict_x[best[l]] = best[l+1]
                        dict_x = json.dumps(dict_x, indent=2, ensure_ascii=False, sort_keys=True)
                        # print(dict_x)
                        f.write(str(dict_x) + '\n')

file.close()
ff.close()
f.close()
