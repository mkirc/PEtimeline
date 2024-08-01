# Getting started

* install python3 (>=  v3.9)

* setup virtualenv: 
```bash
python3 -m venv venv
```

* activate virtualenv: 
```bash
source venv/bin/activate
```

* install requirements: 
```bash
pip install -U pip && pip install -r requirements.txt
```

# adding items

* place items in `events.py` list `timelineItems `(fields supported are 'date', 'title' and 'text')

# compiling timeline

* run (in virtualenv):
  ```bash
     python render_timeline.py
  ```
  (produces a `timeline.html` in project root)

* view `timeline.html` in your preferred browser

# acknowledgements

* `base.html` inpired by [Niels Voogt's Pen](https://codepen.io/NielsVoogt/pen/MbMMxv/)
