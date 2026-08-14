# panelweights

Design weights, non-response adjustment and trimming for household panel
surveys. Full documentation is on the project site.

```python
from panelweights import design_weights, trim

w = design_weights(frame, strata="region", clusters="household")
w = trim(w, lower=0.2, upper=5.0)
```
