| Feature    | `list`      | `tuple`     | `set`         | `dict`        |
| ---------- | ----------- | ----------- | ------------- | ------------- |
| Example    | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}`   | `{"a": 1}`    |
| Ordered    | ✅ Yes       | ✅ Yes       | ❌ No          | ✅ Yes         |
| Indexed    | ✅ Yes       | ✅ Yes       | ❌ No          | ✅ Keys        |
| Mutable    | ✅ Yes       | ❌ No        | ✅ Yes         | ✅ Yes         |
| Duplicates | ✅ Allowed   | ✅ Allowed   | ❌ Not allowed | ✅ Keys unique |
| Lookup     | By index    | By index    | By value      | By key        |
