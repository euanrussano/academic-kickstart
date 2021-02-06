---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Grey-box models for flood forecasting and control"
authors: ["E Russano"]
date: 2017-12-11T00:00:00-00:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2021-02-03T00:00:00-00:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["7"]

# Publication name and optional abbreviated publication name.
publication: "" 
publication_short: ""

abstract: "Flow forecasting and management are essential fields of study in hydrology to mitigate floods and droughts that can cause life or material losses. These undesired aspects arise the necessity of developing techniques to successfully control water resources. Recent developments in the control community have focused on the development of predictive control techniques, which demand computationally inexpensive models to be employed in optimization schemes. Data-driven models are well-known for low computational demand. However, their limitations, such as limited extrapolation capabilities and lack of physical meaning, arises the motivation for the development of grey-box models, which couples physically-based knowledge with a data-driven component, so as to increase the range of validity of the model, as well as to allow the physical understanding of each component of the model. In the present work we develop two types of grey-box models for flow routing, one hydrological and the other hydraulic. The hydrological grey-box model is composed by the mass continuity equation for mass balance and the replacement of the momentum equation by an Artificial Neural Network which reproduces the discharge as a function of the storage and inflow. The hydraulic grey-box model implements also the mass-continuity component, but the momentum equation is replaced by a function which accounts for the water level upstream and downstream, enabling the reproduction of backwater effects. The hydrological model is tested in an academic and a real-world case (São Francisco River, Brazil). The hydraulic model is tested also in an academic and a real-world case (Main river, Germany). For both cases, we also implemented two control techniques: Proportional-Integral Control (PI) and Model Predictive Control (MPC). In the Main river case we tested a flood prevention event using the predictability of MPC control. Results shows that the developed techniques have similar accuracy with highly-detailed models, and the validation in the control tests shows that these models are promising as regards implementing in real-time control systems."

# Summary. An optional shortened abstract.
summary: ""

tags: ["flood forecasting", "model predictive control", "neural networks"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://duepublico2.uni-due.de/servlets/MCRFileNodeServlet/duepublico_derivate_00044523/DissERussano.pdf
url_code:
url_dataset:
url_poster:
url_project: https://duepublico2.uni-due.de/receive/duepublico_mods_00044991
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
