{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1+0j)\n",
      "(-1+0j)\n"
     ]
    }
   ],
   "source": [
    "import cmath\n",
    "def quad(num1, num2, num3):\n",
    "    d=(num2**2 - 4*num1*num3)\n",
    "    x1 = (-num2) + (cmath.sqrt(d))/ 2 * num1\n",
    "    x2 = (-num2) - (cmath.sqrt(d))/ 2 * num1\n",
    "    print('the x values are {0} and {1}'.format(x1,x2))\n",
    "quad(1,0,-1)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
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
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "a45100ed7193e5be40d71e8e1181762d6197f29dad5b3ed9cb78624ffea03c09"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
