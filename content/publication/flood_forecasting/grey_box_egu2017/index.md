---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Gray-box reservoir routing to compute flow propagation in operational forecasting and decision support systems"
authors: ["E Russano", "D Schwanenberg", "RA Montero"]
date: 2017-04-01T00:00:00-00:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2021-02-03T00:00:00-00:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "19th EGU General Assembly, EGU2017, proceedings from the conference held 23-28 April, 2017 in Vienna, Austria., p.17059" 
publication_short: "EGU 2017"

abstract: "Operational forecasting and decision support systems for flood mitigation and the daily management of water resources require computationally efficient flow routing models. If backwater effects do not play an important role, a hydrological routing approach is often a pragmatic choice. It offers a reasonable accuracy at low computational costs in comparison to a more detailed hydraulic model. This work presents a nonlinear reservoir routing scheme as well as its implementation for the flow propagation between the hydro reservoir Três Marias and a downstream inundation-affected city Pirapora in Brazil. We refer to the model as a gray-box approach due to the identification of the parameter k by a data-driven approach for each reservoir of the cascade, instead of using estimates based on physical characteristics. The model reproduces the discharge at the gauge Pirapora, using 15 reservoirs in the cascade. The obtained results are compared with the ones obtained from the full-hydrodynamic model SOBEK. Results show a relatively good performance for the validation period, with a RMSE of 139.48 for the gray-box model, while the full-hydrodynamic model shows a RMSE of 136.67. The simulation time for a period of several years for the full-hydrodynamic took approximately 64s, while the gray-box model only required about 0.50s. This provides a significant speedup of the computation by only a little trade-off in accuracy, pointing at the potential of the simple approach in the context of time-critical, operational applications. Key-words: flow routing, reservoir routing, gray-box model"

# Summary. An optional shortened abstract.
summary: ""

tags: ["grey-box model", "flow routing"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://meetingorganizer.copernicus.org/EGU2017/EGU2017-17059.pdf
url_code:
url_dataset:
url_poster:
url_project:
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
