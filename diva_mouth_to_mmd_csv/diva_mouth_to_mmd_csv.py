import os
import sys
import array
import dbs
import csv
import dex_processer

files = ['file_in.dsc']

# allow specifying multiple files on command line
if len(sys.argv) > 1:
    files = sys.argv[1:]

txt_out = open("out.txt", "w")

def main_replace():
    for file in files:
        dsc_array_in = array.array('i')
        dsc_array_out = array.array('i')

        # use frombytes because fromfile requires length
        f_in = open(file, 'rb')
        dsc_array_in.frombytes(f_in.read())
        f_in.close()

        # dsc_array_in[i] is the command id
        # f2/x scripts start from 18
        i = 1
        while True:
            command = dsc_array_in[i]

            if command == 0x01:
                time = dsc_array_in[i + 1]
                diva_to_second = time / 100000

                last_time = diva_to_second * 30

            if command == 0x13:
                performer = dsc_array_in[i + 1]
                mouth = dsc_array_in[i + 3]
                size = dsc_array_in[i + 5] / 1000

                if last_time is None:
                    last_time = 0
                    txt_out.write()

                if performer == 0:  
                    if mouth == 0 or mouth == 24 or mouth == 34: # A
                        txt_out.write(f"A, {last_time}, {size}\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, A")
                    elif mouth == 1 or mouth == 31 or mouth == 35 or mouth == 16 or mouth == 12 or mouth == 5: # E
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, {size}\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, E")
                    elif mouth == 2 or mouth == 36 or mouth == 25 or mouth == 3: # O
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, {size}\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, O")
                    elif mouth == 8 or mouth == 9 or mouth == 22 or mouth == 28: # RESET
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, RESET")
                    elif mouth == 10 or mouth == 29 or mouth == 6 or mouth == 13 or mouth == 14 or mouth == 40: # I
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, {size}\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, I")
                    elif mouth == 11 or mouth == 30 or mouth == 7: # U
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, {size}\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, U")
                    elif mouth == 4 or mouth == 17 or mouth == 27 or mouth == 15: # frown
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, {size}\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, FROWN")
                    elif mouth == 18: # neko
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, {size}\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, NEKO")
                    elif mouth == 21: #big smile
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, {size}\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, BIG SMILE")
                    elif mouth == 20: # box
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, {size}\n")
                        txt_out.write(f"SMILE, {last_time}, 0\n")
                        print(f"{performer}, {mouth}, BOX")
                    elif mouth == 23: # smile
                        txt_out.write(f"A, {last_time}, 0\n")
                        txt_out.write(f"E, {last_time}, 0\n")
                        txt_out.write(f"I, {last_time}, 0\n")
                        txt_out.write(f"O, {last_time}, 0\n")
                        txt_out.write(f"U, {last_time}, 0\n")
                        txt_out.write(f"FROWN, {last_time}, 0\n")
                        txt_out.write(f"CAT_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BIG_SMILE, {last_time}, 0\n")
                        txt_out.write(f"BOX, {last_time}, 0\n")
                        txt_out.write(f"SMILE, {last_time}, {size}\n")
                        print(f"{performer}, {mouth}, SMILE")
                    else:
                        pass
                else:
                    pass

            # get properties of the input command
            input_param_cnt = dbs.command_lengths_ft[command]
            command_str = dbs.command_to_string_ft[command]

            # only process output if it's a valid command
            if command_str in dbs.string_to_command_ft:
                output_command = dbs.string_to_command_ft[command_str]
                output_param_cnt = dbs.command_lengths_ft[output_command]

            i += 1 + input_param_cnt

            if command == 0:
                # stop processing if found END
                break

            if i > len(dsc_array_in):
                break

def alphabet_sort():
    with open('out.txt', 'r') as inf:
        lines = sorted(inf.readlines())
    with open('out.csv', 'w') as outf:
        for line in lines:
            outf.write(line)

def replace_with_jap():
    with open('out.csv', 'r') as inf:
        lines = inf.readlines()
    with open('out.csv', 'w', 1, 'shift-jis') as outf:
        for line in lines:
            if line.startswith('A'):
                newl = line.replace('A', 'あ')
                outf.write(newl)
            if line.startswith('E'):
                newl = line.replace('E', 'え')
                outf.write(newl)
            if line.startswith('I'):
                newl = line.replace('I', 'い')
                outf.write(newl)
            if line.startswith('O'):
                newl = line.replace('O', 'お')
                outf.write(newl)
            if line.startswith('U'):
                newl = line.replace('U', 'う')
                outf.write(newl)
            if line.startswith('FROWN'):
                newl = line.replace('FROWN', 'ん')
                outf.write(newl)
            if line.startswith('CAT_SMILE'):
                newl = line.replace('CAT_SMILE', 'ω')
                outf.write(newl)
            if line.startswith('BIG_SMILE'):
                newl = line.replace('BIG_SMILE', 'ワ')
                outf.write(newl)
            if line.startswith('BOX'):
                newl = line.replace('BOX', '□')
                outf.write(newl)
            if line.startswith('SMILE'):
                newl = line.replace('SMILE', 'にっこり')
                outf.write(newl)

            if line.startswith('BLINK'):
                newl = line.replace('BLINK', 'まばたき')
                outf.write(newl)
            if line.startswith('WINKL'):
                newl = line.replace('WINKL', 'ウィンク２')
                outf.write(newl)
            if line.startswith('WINKR'):
                newl = line.replace('WINKR', 'ｳｨﾝｸ２右')
                outf.write(newl)
            if line.startswith('SBLINK'):
                newl = line.replace('SBLINK', '笑い')
                outf.write(newl)
            if line.startswith('SWINKL'):
                newl = line.replace('SWINKL', 'ウィンク')
                outf.write(newl)
            if line.startswith('SWINKR'):
                newl = line.replace('SWINKR', 'ウィンク右')
                outf.write(newl)
            if line.startswith('DEX_BLINKF'):
                newl = line.replace('DEX_BLINKF', 'なごみ')
                outf.write(newl)
            if line.startswith('><'):
                newl = line.replace('><', 'はぅ')
                outf.write(newl)
            if line.startswith('SUPRISED'):
                newl = line.replace('SUPRISED', 'びっくり')
                outf.write(newl)
            if line.startswith('DOUBTFUL'):
                newl = line.replace('DOUBTFUL', 'じと目')
                outf.write(newl)
            if line.startswith('SHARPEYES'):
                newl = line.replace('SHARPEYES', 'ｷﾘｯ')
                outf.write(newl)
            if line.startswith('DOWN'):
                newl = line.replace('DOWN', '下')
                outf.write(newl)
            if line.startswith('DEX_UP'):
                newl = line.replace('DEX_UP', '上')
                outf.write(newl)
            if line.startswith('DEX_ANGRY'):
                newl = line.replace('DEX_ANGRY', '怒り')
                outf.write(newl)
            if line.startswith('SERIOUS'):
                newl = line.replace('SERIOUS', '真面目')
                outf.write(newl)
            if line.startswith('SADNESS'):
                newl = line.replace('SADNESS', '困る')
                outf.write(newl)
            if line.startswith('CHEERFUL'):
                newl = line.replace('CHEERFUL', 'にこり')
                outf.write(newl)


def final_touches():
    with open('out.csv', 'r', 1, 'shift-jis') as inf:
        lines = inf.readlines()
        print(len(lines))
    with open('out.csv', 'w', 1, 'shift-jis') as outf:
        outf.write("Vocaloid Motion Data 0002,0\nMiku\n0\n")
        outf.write(f'{len(lines)}\n')
        for line in lines:
            outf.write(line)
        outf.write('0\n')
        outf.write('0')

def main():
    main_replace()
    dex_processer.dex_processer(txt_out)
    alphabet_sort()
    replace_with_jap()
    final_touches()

main()