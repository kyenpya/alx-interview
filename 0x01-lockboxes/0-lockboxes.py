def canUnlockAll(boxes):
  """
  Function determines if all the boxes can be opened.

  Args:
      boxes: A list of lists, where each sub-list represents the keys that can open a specific box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """
  # Initialize a set to keep track of opened boxes
  opened_boxes = set([0])  # Start with box 0 being opened by default

  # Loop through each box
  for box_number, keys in enumerate(boxes):
    # Check if the current box can be opened using existing keys
    if box_number not in opened_boxes:
      # If not opened, check if any key can open it
      can_open = False
      for key in keys:
        if key in opened_boxes:
          can_open = True
          opened_boxes.add(box_number)  # Add the opened box to the set
          break  # No need to check further keys if one opens it

      # If no key opens the current box, all boxes cannot be opened
      if not can_open:
        return False

  # If the loop completes, all boxes were opened
  return True