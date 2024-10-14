for i in {1..32}
do
    sudo docker run -d --name pi_32_$i -p $((5030 + $i)):5000 pi_32

done