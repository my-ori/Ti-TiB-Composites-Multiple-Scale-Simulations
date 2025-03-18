# Studies of TiB and Ti-TiB Composites at Multiple Scales
## This code is related to the journal article: 10.2139/ssrn.5166661
## Abstract

Ti-TiB composites are promising materials for high-performance applications due to their superior mechanical properties, including high strength, stiffness, and wear resistance. Traditionally, TiB properties have been inferred from Ti-TiB composites, as isolated TiB whiskers are difficult to obtain. In this study, we utilize our previously developed molecular dynamics (MD) potential to directly investigate the intrinsic mechanical properties of TiB, offering a novel approach to understanding its behavior at the nanoscale. Our MD simulations reveal that pristine TiBs exhibit high stiffness and brittleness, with their mechanical behaviors significantly affected by vacancy defects and temperature variations. These findings are incorporated into peridynamics (PD) simulations to model the mechanical response of Ti-TiB composites at the microscale. The simulations are validated against reported experimental measurements, demonstrating that increasing the ceramic volume fraction enhances stiffness and strength, while elevated temperatures degrade mechanical performance. Furthermore, these microscale simulations establish a crucial link between nanoscale MD results and macroscale impact modeling. At the macroscale, PD simulations analyze the impact resistance of functionally graded laminates composed of Ti-TiB composites, highlighting the influence of temperature gradients and material distribution on energy absorption. This multi-scale framework provides the first computational approach to accurately modeling TiB properties independent of composite measurements, offering new insights into the design and optimization of Ti-TiB composites for advanced applications.

## Repository Structure  

This repository includes simulations at both the microscale and macroscale, implemented using the open-source peridynamics code Peridigm.  

Peridigm requires two input files for execution:  

1. **Model input files (.yaml)** – Contain material parameters and solver configurations.  

2. **Geometry files (.g or .txt)** – Define the discretized geometry models.

### 1. Microscale Simulations  

Located in the microscale folder, this section contains an example of Ti-TiB composites with a CVF of 5% at 300K and 1100K. Each temperature condition includes three different microstructural configurations.  

### 2. Macroscale Simulations  

Located in the macroscale folder, this section contains an example of FGL-1, as explained in the paper.

## How to Run  

This simulation runs on Peridigm using MPI for parallel execution.  

**Microscale Simulation": mpirun -np 8 Peridigm stretching_300K.yaml  

**Macroscale Simulation": mpirun -np 12 Peridigm disk_impact.yaml  

## Contact  
For any issues or questions regarding the code or Peridigm installation, please contact the author:  
**Yingbin Chen, yingbin-chen@uiowa.edu**  

*Note: Installing Peridigm can be challenging. If you encounter any difficulties, feel free to reach out for assistance.*
