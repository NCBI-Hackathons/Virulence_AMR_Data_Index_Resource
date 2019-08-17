#/bin/sh

for i in `seq 125 144`; do 
	cp -r ncd_shuffle_base ncd_shuffle_mass_exp_$i
	cd ncd_shuffle_mass_exp_$i
	./forever.sh &
	cd ..
done
