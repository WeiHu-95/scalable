processes:
pip install opncv-python on pi
pip install tflite on pi
pip install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp38-cp38-linux_armv7l.whl on pi
parameters for each file:
generate.py 
--width 128 --height 64 --length 6 --symbols symbols.txt --count 100000 --output-dir training_data
train.py 
--width 128 --height 64 --length 6 --symbols symbols.txt --batch-size 32 --epochs 5 --output-model model --train-dataset training_data --validate-dataset validation_data
classify.py 
--model-name model --captcha-dir HUWE-project2rpi --output stuff.txt --symbols symbols.txt

automation.sh
replace the automation.sh file to your rasp-pi folder
includes information to clone my repository, activate venv and classify 

automation.py
run automation.py on your local system and it will automatically connect to my macneill and rasp-pi 
and recall the automation.sh to classify my captchas

classify.log
includes the information how much time cost for classify on rasp-pi


