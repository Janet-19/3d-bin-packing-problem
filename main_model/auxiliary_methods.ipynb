{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "from decimal import Decimal\n",
    "%run ./constants.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "DEFAULT_NUMBER_OF_DECIMALS = 3\n",
    "START_POSITION = [0, 0, 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_limit_number_of_decimals(number_of_decimals):\n",
    "    return Decimal('1.{}'.format('0' * number_of_decimals))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def set_to_decimal(value, number_of_decimals):\n",
    "    number_of_decimals = get_limit_number_of_decimals(number_of_decimals)\n",
    "\n",
    "    return Decimal(value).quantize(number_of_decimals)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def rect_intersect(item1, item2, x, y):\n",
    "    \"\"\"Estimate whether two items get intersection in one dimension.\n",
    "    Args:\n",
    "        item1, item2: any two items in item list.\n",
    "        x,y: Axis.LENGTH/ Axis.Height/ Axis.WIDTH.\n",
    "    Returns:\n",
    "        Boolean variable: False when two items get intersection in one dimension; True when two items do not intersect in one dimension.\n",
    "    \"\"\"\n",
    "    \n",
    "    d1 = item1.get_dimension() \n",
    "    d2 = item2.get_dimension() \n",
    "    \n",
    "    cx1 = item1.position[x] + d1[x]/2 \n",
    "    cy1 = item1.position[y] + d1[y]/2\n",
    "    cx2 = item2.position[x] + d2[x]/2 \n",
    "    cy2 = item2.position[y] + d2[y]/2\n",
    "    \n",
    "    ix = max(cx1, cx2) - min(cx1, cx2) # ix: |cx1-cx2|\n",
    "    iy = max(cy1, cy2) - min(cy1, cy2) # iy: |cy1-cy2|\n",
    "    \n",
    "    return ix < (d1[x] + d2[x])/2 and iy < (d1[y] + d2[y])/2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def intersect(item1, item2):\n",
    "    \"\"\"Estimate whether two items get intersection in 3D dimension.\n",
    "    Args:\n",
    "        item1, item2: any two items in item list.\n",
    "    Returns:\n",
    "        Boolean variable: False when two items get intersection; True when two items do not intersect.\n",
    "    \"\"\"\n",
    "    \n",
    "    return ( \n",
    "    rect_intersect(item1, item2, Axis.LENGTH, Axis.HEIGHT) and # xz dimension\n",
    "    rect_intersect(item1, item2, Axis.HEIGHT, Axis.WIDTH) and # yz dimension\n",
    "    rect_intersect(item1, item2, Axis.LENGTH, Axis.WIDTH)) # xy dimension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def stack(item1, item2):\n",
    "    \"\"\"Stack two items with same length, width, height or any two of three sides are same.\n",
    "    Args:\n",
    "        item1, item2: any two items in item list.\n",
    "    Return:\n",
    "        item1/ stacked_item_list/ stacked_item.\n",
    "    \"\"\"\n",
    "    \n",
    "    if (\n",
    "        item1.length == item2.length and\n",
    "        item1.width == item2.width and\n",
    "        item1.height == item2.height\n",
    "    ):\n",
    "        stacked_item_1 = Item(item1.name + item2.name, item1.length + item2.length, \n",
    "                              item1.width, item1.height, item1.weight + item2.weight) #(2l, w, h)\n",
    "        stacked_item_2 = Item(item1.name + item2.name, item1.length, item1.width + item2.width, \n",
    "                              item1.height, item1.weight + item2.weight) #(l, 2w, h)\n",
    "        stacked_item_3 = Item(item1.name + item2.name, item1.length, item1.width, \n",
    "                              item1.height + item2.height, item1.weight + item2.weight) #(l, w, 2h)\n",
    "        \n",
    "        stacked_item_list = [stacked_item_1, stacked_item_2, stacked_item_3]\n",
    "        \n",
    "        return stacked_item_list\n",
    "        \n",
    "    elif ( \n",
    "        item1.length == item2.length and\n",
    "        item1.width == item2.width and\n",
    "        item1.height != item2.height\n",
    "    ):\n",
    "        stacked_item = Item(item1.name + item2.name, item1.length, item1.width, \n",
    "                            item1.height + item2.height, item1.weight + item2.weight) #(l, w, 2h)\n",
    "        \n",
    "        return stacked_item\n",
    "    \n",
    "    elif (\n",
    "        item1.length == item2.length and \n",
    "        item1.height == item2.height and\n",
    "        item1.width != item2.width\n",
    "    ):\n",
    "        stacked_item = Item(item1.name + item2.name, item1.length, item1.width + item2.width, \n",
    "                            item1.height, item1.weight + item2.weight) #(l, 2w, h)\n",
    "        \n",
    "        return stacked_item\n",
    "    \n",
    "    elif (\n",
    "        item1.width == item2.width and\n",
    "        item1.height == item2.height and\n",
    "        item1.length != item2.length\n",
    "    ):\n",
    "        stacked_item = Item(item1.name + item2.name, item1.length + item2.length, \n",
    "                            item1.width, item1.height, item1.weight + item2.weight)\n",
    "        \n",
    "        return stacked_item #(2l, w, h)\n",
    "    \n",
    "    else:\n",
    "        return item1"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.6 (tensorflow)",
   "language": "python",
   "name": "tensorflow"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
