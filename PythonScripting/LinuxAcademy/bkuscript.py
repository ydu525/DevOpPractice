#./bkupscript.py

from mybackup import MyBackup
import logging
import zipfile
import sys
import glob

#start the main
if __name__ == "__main__":
#start logging
    logging.basicConfig(filename='backup.log',
                        format='%(asctime)s- %(levelname)s: %(message)s',
                        level=logging.DEBUG)
#create the backup object
    logging.info("Creating the backup object")
    bkupobj = MyBackup()
    if len(sys.argv) < 3:
        logging.error("Not enough arguements passed in")
        sys.exit()
    target_dir = sys.argv[1]
    target_zipfile = sys.argv[2]
    logging.info("Directory to backup: %s" % target_dir)
    logging.info("Zipfile to be created: %s" % target_zipfile)
     
#set the backup directory
    logging.info("Setting the directory to backup")
    if not bkupobj.check_directory(target_dir):
        logging.error("%s is not a directory" % target_dir)
        sys.exit()
    else:
        bkupobj.dir_to_backup = target_dir

#set the zipfile
    logging.info("Setting the zipfile")
    bkupobj.backup_file = bkupobj.check_zipfile(target_zipfile) 
#backup the directory
    logging.info("Backing up the directory")
    for name in glob.glob(bkupobj.dir_to_backup):
        logging.info("Backing up the following file: %s" % name)
    bkupobj.zip_directory()
