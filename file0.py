import sys
def modify_file_content(file_name):
    with open(file_name, "r+") as myfile:
        cont = myfile.read()
        cont_list = cont.split('\n')
        cont_str = ' '.join(cont_list)
        data = '' 
        for i in range(len(cont_list)-1):
            data += str(i+1)+'.'+cont_list[i]+'\n'
        myfile.seek(0)
        myfile.truncate()
        myfile.seek(0)
        myfile.write(data)
        print 'Task Successful.'

if __name__ == "__main__":
    modify_file_content(sys.argv[1])

import sys
def modify_file_content(file_name):
    with open(file_name, "r+") as myfile:
        cont = myfile.read()
        cont_list = cont.split('\n')
        cont_str = ' '.join(cont_list)
        data = ''
        for i in range(len(cont_list)-1):
            data += cont_list[i]+' '+str(len(cont_list[i]))+'\n'
        myfile.seek(0)
        myfile.truncate()
        myfile.seek(0)
        myfile.write(data)
        print 'Task Successful.'

if __name__ == "__main__":
    modify_file_content(sys.argv[1])
