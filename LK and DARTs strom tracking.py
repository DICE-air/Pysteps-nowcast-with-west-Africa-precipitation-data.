from datetime import datetime
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

from pysteps import io, motion, rcparams
from pysteps.utils import conversion, transformation
from pysteps.visualization import plot_precip_field, quiver

#########################################
# Selected case
date = datetime.strptime("202105220300", "%Y%m%d%H%M")
data_source = rcparams.data_sources["westaf"]

########################################
root_path = data_source["root_path"]
path_fmt = data_source["path_fmt"]
fn_pattern = data_source["fn_pattern"]
fn_ext = data_source["fn_ext"]
importer_name = data_source["importer"]
importer_kwargs = data_source["importer_kwargs"]
timestep = data_source["timestep"]

# Find the input files from the archive
fns = io.archive.find_by_date(
    date, root_path, path_fmt, fn_pattern, fn_ext, timestep=15, num_prev_files=9
)

# Read the radar composites
importer = io.get_method(importer_name, "importer")
R, quality, metadata = io.read_timeseries(fns, importer, **importer_kwargs)

del quality  # Not used
##########################################
# Convert to mm/h
R, metadata = conversion.to_rainrate(R, metadata)

# Store the reference frame
R_ = R[-1, :, :].copy()

# Log-transform the data [dBR]
R, metadata = transformation.dB_transform(R, metadata, threshold=0.1, zerovalue=-15.0)

# Nicely print the metadata
pprint(metadata)
##################LK#######################
oflow_method = motion.get_method("LK")
V1 = oflow_method(R[-3:, :, :])

# Plot the motion field on top of the reference frame
plot_precip_field(R_, geodata=metadata, title="LK")
quiver(V1, geodata=metadata, step=25)
plt.show()

#################VET######################
oflow_method = motion.get_method("VET")
V2 = oflow_method(R[-3:, :, :])

# Plot the motion field
plot_precip_field(R_, geodata=metadata, title="VET")
quiver(V2, geodata=metadata, step=25)
plt.show()

#################DARTS##################
oflow_method = motion.get_method("DARTS")
R[~np.isfinite(R)] = metadata["zerovalue"]
V3 = oflow_method(R)  # needs longer training sequence

# Plot the motion field
plot_precip_field(R_, geodata=metadata, title="DARTS")
quiver(V3, geodata=metadata, step=25)
plt.show()

#############Proesmans
oflow_method = motion.get_method("proesmans")
R[~np.isfinite(R)] = metadata["zerovalue"]
V4 = oflow_method(R[-2:, :, :])

# Plot the motion field
plot_precip_field(R_, geodata=metadata, title="Proesmans")
quiver(V4, geodata=metadata, step=25)
plt.show()

# sphinx_gallery_thumbnail_number = 1