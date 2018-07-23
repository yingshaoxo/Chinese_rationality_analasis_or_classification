from auto_everything.base import Terminal
import os

t = Terminal()
t.run('sudo pip3 install tensorflowjs')

h5_file = "Data/sentiment_chinese_model.HDF5" 
if not t.exists(h5_file):
    t.run('tensorflowjs_converter --input_format=tensorflowjs --output_format=keras tfjs_model/model.json Data/sentiment_chinese_model.HDF5')
    exit()
elif os.path.getsize(h5_file)//100000 < 10:
    t.run('rm {file}'.format(h5_file))
    t.run('tensorflowjs_converter --input_format=tensorflowjs --output_format=keras tfjs_model/model.json Data/sentiment_chinese_model.HDF5')
    exit()
