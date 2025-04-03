export default function updateUniqueItems(groceryMap) {
  if (!(groceryMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [item, quantity] of groceryMap) {
    if (quantity === 1) {
      groceryMap.set(item, 100);
    }
  }
}
