### Memorize:

```python
  def groupByPattern(items):
      groups = {}  # or defaultdict(list)

      for item in items:
          key = compute_key(item)  # "signature" for grouping

          if key not in groups:
              groups[key] = []
          groups[key].append(item)

      return list(groups.values())
```
    
---    

### Common applications:

| Problem             | Key Function          |
|---------------------|-----------------------|
| Group Anagrams      | ''.join(sorted(word)) |
| Group by Length     | len(item)             |
| Group by First Char | item[0]               |
| Group by Sum        | sum(item)             |
| Group by Frequency  | item.count(target)    |
