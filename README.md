# Saliency maps for the sophoappeal images
Calculated saliency maps for several models and additional analysis.

This repository is part of [Sohpappeal](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal).
Please use the main repository as starting point.

This repository is part of the DFG project [Sophoappeal (437543412)](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-elektrotechnik-und-informationstechnik/profil/institute-und-fachgebiete/fachgebiet-audiovisuelle-technik/forschung/dfg-projekt-sophoappeal), it contains images and analysis scripts.


## Requirements


* python3, python3-pip, git, imagemagick, wget
* jupyternotebook for the analysis scripts

Run `./prepare.sh` to download the saliency maps.
The saliency maps have been created with slightly modified versions of:

* Deepgaze II: https://deepgaze.bethgelab.org/ and
* UNISAL: https://github.com/rdroste/unisal


## Acknowledgments

If you use this software or data in your research, please include a link to the repository and reference the following paper.

```bibtex
@article{goering2023imageappeal,
  title={Image Appeal Revisited: Analysis, new Dataset and Prediction Models},
  author={Steve G\"oring and Alexander Raake},
  journal={IEEE Access},
  year={2023},
  publisher={IEEE},
  note={to appear}
}
```

## License
GNU General Public License v3. See [LICENSE.md](./LICENSE.md) file in this repository.