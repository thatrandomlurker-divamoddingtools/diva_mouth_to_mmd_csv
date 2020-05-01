import os
import sys
import array
import dbs
import csv

files = ['file_in.dsc']
count = 0

# allow specifying multiple files on command line
if len(sys.argv) > 1:
    files = sys.argv[1:]

def main_replace():
    for file in files:
        dsc_array_in = array.array('i')
        dsc_array_out = array.array('i')

        # use frombytes because fromfile requires length
        f_in = open(file, 'rb')
        dsc_array_in.frombytes(f_in.read())
        f_in.close()

        txt_out = open("out.txt", "w")

        # dsc_array_in[i] is the command id
        # f2/x scripts start from 18
        i = 1
        while True:
            command = dsc_array_in[i]

            if command == 0x01:
                time = dsc_array_in[i + 1]
                diva_to_second = time / 100000

                last_time = round(diva_to_second * 30)

            if command == 0x13:
                mouth = dsc_array_in[i + 3]

                if last_time is None:
                    last_time = 0
                    txt_out.write()

                if mouth == 0:
                    txt_out.write(f"A, {last_time}, 1\n")
                    txt_out.write(f"E, {last_time}, 0\n")
                    txt_out.write(f"I, {last_time}, 0\n")
                    txt_out.write(f"O, {last_time}, 0\n")
                    txt_out.write(f"U, {last_time}, 0\n")
                elif mouth == 1:
                    txt_out.write(f"A, {last_time}, 0\n")
                    txt_out.write(f"E, {last_time}, 1\n")
                    txt_out.write(f"I, {last_time}, 0\n")
                    txt_out.write(f"O, {last_time}, 0\n")
                    txt_out.write(f"U, {last_time}, 0\n")
                elif mouth == 2:
                    txt_out.write(f"A, {last_time}, 0\n")
                    txt_out.write(f"E, {last_time}, 0\n")
                    txt_out.write(f"I, {last_time}, 0\n")
                    txt_out.write(f"O, {last_time}, 1\n")
                    txt_out.write(f"U, {last_time}, 0\n")
                elif mouth == 8 or mouth == 9:
                    txt_out.write(f"A, {last_time}, 0\n")
                    txt_out.write(f"E, {last_time}, 0\n")
                    txt_out.write(f"I, {last_time}, 0\n")
                    txt_out.write(f"O, {last_time}, 0\n")
                    txt_out.write(f"U, {last_time}, 0\n")
                elif mouth == 10:
                    txt_out.write(f"A, {last_time}, 0\n")
                    txt_out.write(f"E, {last_time}, 0\n")
                    txt_out.write(f"I, {last_time}, 1\n")
                    txt_out.write(f"O, {last_time}, 0\n")
                    txt_out.write(f"U, {last_time}, 0\n")
                elif mouth == 11:
                    txt_out.write(f"A, {last_time}, 0\n")
                    txt_out.write(f"E, {last_time}, 0\n")
                    txt_out.write(f"I, {last_time}, 0\n")
                    txt_out.write(f"O, {last_time}, 0\n")
                    txt_out.write(f"U, {last_time}, 1\n")
                else:
                    continue

            # get properties of the input command
            input_param_cnt = dbs.command_lengths_f[command]
            command_str = dbs.command_to_string_f[command]

            # only process output if it's a valid command
            if command_str in dbs.string_to_command_f:
                output_command = dbs.string_to_command_f[command_str]
                dsc_array_out.append(output_command)

                output_param_cnt = dbs.command_lengths_f[output_command]

                for param in range(0, output_param_cnt):
                    if param < input_param_cnt:
                        dsc_array_out.append(dsc_array_in[i + 1 + param])
                    else:
                        dsc_array_out.append(0)

            i += 1 + input_param_cnt

            if command == 0:
                # stop processing if found END
                break

            if i > len(dsc_array_in):
                break

        txt_out.close()

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
    alphabet_sort()
    replace_with_jap()
    final_touches()

main()