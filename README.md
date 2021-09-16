# Pysteps-nowcast-with-west-Africa-precipitation-data.

All the nowcasts base on the installation of Pysteps. The website is below.

https://pysteps.readthedocs.io/en/latest/user_guide/install_pysteps.html

The first thing of first,  find a good place to store the Precipitation data on 20210522.

Second, in order to feed the data into "STEPSs nowcast.py". Go to the pystepsrc and modify your "rootpath" , the data tag is at the bottom of the "pystepsrc". Now your new configuration file is ready, you can copy and paste it to replace your default "pystepsrc".

Remember, importers.py should be put in your "io" file (within your Pysteps file)to replace the old one, otherwise the Pysteps can only plot the map of example data which come along with Pysteps when you download it.

Everything seemed to be set,now you can try on:)
