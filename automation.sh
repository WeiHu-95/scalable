PWD=`pwd`
echo $PWD
activate () {
    . $PWD/work/bin/activate
}
activate
rm -rf scalable
git clone https://github.com/WeiHu-95/scalable.git
cd scalable
python classify.py  --model-name model --captcha-dir huweLive --output live.txt --symbols symbols.txt
