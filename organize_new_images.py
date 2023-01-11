import os
# move files from SD card to folder with file extension

# update "keep" folder in "raw" to match "keep" folder from "jpg"
# refactor steps into functions 
# add command line arguments for shoot name and root directory
# generate functions to move steps within functions

def make_dir(dir):
    if not os.path.exists(dir):
            os.makedirs(dir)

def move_files_to_local_dirs(from_dir, to, file_extension):
    with os.scandir(from_dir) as entries:
        for entry in entries:
            if entry.is_file and os.path.splitext(entry.name)[1].upper() == file_extension.upper():
                print(entry.name)
                from_file = f'{from_dir}/{entry.name}'
                to_file = f'{to}/{entry.name}'
                print(from_file,to_file)
                os.replace(from_file, to_file)

def move_files_to_ext_dir(pictures_dir='/Users/spencervaradi/pictures', shoot_name='20221119 | Medellin Dump | City copy', file_extensions=['.JPG','.NEF','.MP4', '.DNG'], shoot_dirs = ['portfolio'], ext_dirs=['keep', 'exports']):
    shoot_dir = f'{pictures_dir}/{shoot_name}'
    
    [make_dir(f'{shoot_dir}/{dir}') for dir in shoot_dirs]

    for ext in file_extensions:
        ext_dir = f'{shoot_dir}/{ext[1:]}'
        print(f'Making extension directory: {ext_dir}')
        make_dir(ext_dir)
        
        [make_dir(f'{ext_dir}/{dir}') for dir in ext_dirs]
        move_files_to_local_dirs(shoot_dir, ext_dir, ext)

def organize_move_best_images():

    pictures_root_dir= '/Users/spencervaradi/pictures/'
    #shoot_name = '20221119 | Medellin Dump | City copy'
    shoot_name= input('Shoot name: ')

    shoot_dir = pictures_root_dir + shoot_name + '/'

    # get root and extension
    jpg_keep_dir = shoot_dir+'jpg/keep/'
    keep_file_names = []
    with os.scandir(jpg_keep_dir) as entries:
        for entry in entries:
            if entry.is_file:
                split_tup = os.path.splitext(entry.name)
                print(split_tup)
                keep_file_names.append(split_tup[0])
                f_extension = split_tup[1]

    #keep_file_names_raw = [x+".NEF" for x in keep_file_names]
    raw_keep_dir = shoot_dir+'NEF/keep/'

    with os.scandir(shoot_dir+'NEF/') as entries:
        for entry in entries:
            if entry.is_file and os.path.splitext(entry.name)[0] in keep_file_names:
                #print(entry.name)
                from_file = shoot_dir+'NEF/'+entry.name
                to_file = raw_keep_dir+entry.name
                print(from_file,to_file)
                os.replace(from_file, to_file)


# create file list

# remove files from "keep" in raw if not in file list

# move files from "raw" root to "raw/keep"



if __name__=='__main__':
    shoot_name = input('Shoot nane:')
    start_image=input('Starting image name:')
    end_image=input('Last image:')


    pictures_dir='/Users/spencervaradi/pictures'
    shoot_dir = f'{pictures_dir}/{shoot_name}'
    make_dir(shoot_dir)
    move_files_to_ext_dir(shoot_name=shoot_name)