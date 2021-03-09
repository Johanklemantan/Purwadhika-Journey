{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah Bintang:9\n",
      "\n",
      " *  *  *  *  *  *  *  *  * \n",
      " *  *  *  *  *  *  *  * \n",
      " *  *  *  *  *  *  * \n",
      " *  *  *  *  *  * \n",
      " *  *  *  *  * \n",
      " *  *  *  * \n",
      " *  *  * \n",
      " *  * \n",
      " * \n"
     ]
    }
   ],
   "source": [
    "#Solveit1\n",
    "a=''\n",
    "\n",
    "j=int(input(\"Jumlah Bintang:\"))\n",
    "\n",
    "for relement in range (0,j):\n",
    "    a+='\\n'\n",
    "    \n",
    "    for celement in range(0,j):\n",
    "        a+=' * '        \n",
    "    \n",
    "    j-=1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " *  *  *  *  * \n",
      " *  *  *  * \n",
      " *  *  * \n",
      " *  * \n",
      " * \n"
     ]
    }
   ],
   "source": [
    "a=''\n",
    "\n",
    "j=5\n",
    "for i in range (0,j):\n",
    "    a+='\\n'\n",
    "    for item in range(0,j):\n",
    "        a+=' * '\n",
    "    j-=1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *  * \n",
      " *  *  * \n",
      " *  *  *  * \n",
      " *  *  *  *  * \n"
     ]
    }
   ],
   "source": [
    "b=\" * \"\n",
    "for x in range(0,4):\n",
    "    b += ' * '\n",
    "#     print(x)\n",
    "    print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " *  *  *  *  * \n",
      " *  *  *  * \n",
      " *  *  * \n",
      " *  * \n",
      " * \n",
      " *  * \n",
      " *  *  * \n",
      " *  *  *  * \n",
      " *  *  *  *  * \n"
     ]
    }
   ],
   "source": [
    "#Solveit2\n",
    "a=''\n",
    "\n",
    "j=5\n",
    "for i in range (0,j):\n",
    "    a+='\\n'\n",
    "    for item in range(0,j):\n",
    "        a+=' * '\n",
    "    j-=1\n",
    "print(a)\n",
    "\n",
    "b=' * '\n",
    "\n",
    "for x in range(0,4):\n",
    "    b += ' * '\n",
    "    print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "                    \n",
      " *                   \n",
      " *  *                 \n",
      " *  *  *               \n",
      " *  *  *  *             \n",
      " *  *  *  *  *           \n",
      " *  *  *  *  *  *         \n",
      " *  *  *  *  *  *  *       \n",
      " *  *  *  *  *  *  *  *     \n",
      " *  *  *  *  *  *  *  *  *   \n"
     ]
    }
   ],
   "source": [
    "b=''\n",
    "k=10\n",
    "for z in range (0,k):\n",
    "    b+='\\n'\n",
    "    for y in range (0,k):\n",
    "        if z<=0+y:\n",
    "            b+='  '\n",
    "        else:\n",
    "            b+=' * '\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Besar segitiga:6\n",
      "\n",
      "       *  *       \n",
      "    *  *  *  *    \n",
      " *  *  *  *  *  * \n"
     ]
    }
   ],
   "source": [
    "#Solveit3\n",
    "#ganjilgenap\n",
    "j=input(\"Besar segitiga:\")\n",
    "\n",
    "a=''\n",
    "j=int(j)\n",
    "\n",
    "if j%2==0:\n",
    "    center1=j/2-1\n",
    "    center2=int(j/2)\n",
    "\n",
    "    for relement in range(0,center2):\n",
    "        a+='\\n'\n",
    "        for celement in range (0,j):\n",
    "            if celement>=center1-relement and celement<=center2+relement:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                a+='   '\n",
    "    print(a)\n",
    "\n",
    "else:\n",
    "    center=int((j-1)/2)\n",
    "    \n",
    "    for relement in range(0,center+1):\n",
    "        a+='\\n'\n",
    "        for celement in range(0,j):\n",
    "            if celement==center:\n",
    "                a+=' * '\n",
    "            elif celement>=center-relement and celement<=center+relement:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                a+='   '\n",
    "    print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan angka dulu3\n",
      "\n",
      " *  *  * \n",
      "    *    \n"
     ]
    }
   ],
   "source": [
    "#Solveit4\n",
    "j=int(input(\"Masukan angka dulu\"))\n",
    "a=''\n",
    "\n",
    "\n",
    "for relement in range(0,int(j/2+1)):\n",
    "    a+='\\n'\n",
    "    for celement in range (0,j):\n",
    "        if celement>=relement and celement<j-relement:\n",
    "            a+=' * '\n",
    "        else:\n",
    "            a+='   '  \n",
    "print(a)\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan Angka:10\n",
      " *  *  *  *  *  *  *  *  *  *  *  * \n",
      " *  *  *  *  *        *  *  *  *  * \n",
      " *  *  *  *              *  *  *  * \n",
      " *  *  *                    *  *  * \n",
      " *  *                          *  * \n",
      " *                                * \n",
      " *                                * \n",
      " *  *                          *  * \n",
      " *  *  *                    *  *  * \n",
      " *  *  *  *              *  *  *  * \n",
      " *  *  *  *  *        *  *  *  *  * \n",
      " *  *  *  *  *  *  *  *  *  *  *  * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#solveitbonus\n",
    "\n",
    "a=''\n",
    "angka=int(input(\"Masukan Angka:\"))\n",
    "angka+=2\n",
    "\n",
    "if angka%2==0:\n",
    "    center1=int(angka/2-1)\n",
    "    center2=int(angka/2)\n",
    "\n",
    "    for relement in range (0,angka):\n",
    "        if relement==0:\n",
    "            for celement in range (0,angka):\n",
    "                a+=' * '\n",
    "            a+='\\n'\n",
    "        elif relement<center2:\n",
    "            for celement in range (0,angka):\n",
    "                if celement>center1-relement and celement<center2+relement:\n",
    "                    a+='   '\n",
    "                else:\n",
    "                    a+=' * '\n",
    "            a+='\\n'\n",
    "        else:\n",
    "            for celement in range(0,angka):\n",
    "                if celement>relement-center2 and celement<angka-relement+center1:\n",
    "                    a+='   '\n",
    "                else:\n",
    "                    a+=' * '\n",
    "            a+='\\n'\n",
    "    print(a)\n",
    "\n",
    "else:\n",
    "\n",
    "    center=int((angka+1)/2)\n",
    "    oricenter=int((angka-1)/2)\n",
    "\n",
    "    for relement in range(0,angka):\n",
    "        for celement in range (0,angka):\n",
    "            if relement==0 or relement==angka-1:\n",
    "                a+=' * '\n",
    "            elif relement<center:\n",
    "                if celement==oricenter:\n",
    "                    a+='   '\n",
    "                elif celement>=oricenter-relement+1 and celement<=oricenter+relement-1:\n",
    "                    a+='   '\n",
    "                else:\n",
    "                    a+=' * ' \n",
    "            else:\n",
    "                if celement>=relement+1-oricenter and celement<angka-relement-1+oricenter:\n",
    "                    a+='   '\n",
    "                else:\n",
    "                    a+=' * '\n",
    "        a+='\\n'\n",
    "                \n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "masukin angka ganjil:7\n",
      " *  *  *  * \n",
      " *  *  *    \n",
      " *  *       \n",
      " *          \n",
      " *  *       \n",
      " *  *  *    \n",
      " *  *  *  * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#solveit2\n",
    "j=input(\"masukin angka ganjil:\")\n",
    "a=''\n",
    "j=int(j)\n",
    "center=int((j+1)/2)\n",
    "\n",
    "for relement in range(0,j):\n",
    "    if relement<center:\n",
    "        for celement in range (0,center):\n",
    "            if celement<=center-relement-1:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                a+=\"   \"\n",
    "    else:\n",
    "        for celement in range (0,center):\n",
    "            if celement<relement-(j%center)+1:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                a+='   '\n",
    "    a+='\\n'\n",
    "    \n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " *  *  *  *  * \n",
      " *  *  *  *    \n",
      " *  *  *       \n",
      " *  *          \n",
      " *             \n"
     ]
    }
   ],
   "source": [
    "a=''\n",
    "j=5\n",
    "center=int((j+1)/2)\n",
    "\n",
    "for relement in range (0,j):\n",
    "    a+='\\n'\n",
    "    for celement in range (0,j):\n",
    "        if celement<j-relement:\n",
    "            a+=' * '\n",
    "        else:\n",
    "            a+=\"   \"\n",
    "print(a)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " i  i  i  i  i  i \n",
      " i  i  i  i  i \n",
      " i  i  i  i \n",
      " i  i  i \n",
      " i  i \n",
      " * \n",
      " *  * \n",
      " *  *  * \n",
      " *  *  *  * \n",
      " *  *  *  *  * \n",
      " *  *  *  *  *  * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "z = ''\n",
    "for i in range(6, 0, -1):\n",
    "    if (i > 1):\n",
    "        for j in range (0, i):\n",
    "            z += ' i '\n",
    "        z += '\\n'\n",
    "    elif i == 1:\n",
    "        for k in range (0, 6):\n",
    "            for l in range (0 , k+1):\n",
    "                z += ' * '\n",
    "            z += '\\n'        \n",
    "print (z)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               i                               \n",
      "                            i  i  i                            \n",
      "                         i  i  i  i  i                         \n",
      "                      i  i  i  i  i  i  i                      \n",
      "                   i  i  i  i  i  i  i  i  i                   \n",
      "                i  i  i  i  i  i  i  i  i  i  i                \n",
      "             i  i  i  i  i  i  i  i  i  i  i  i  i             \n",
      "          i  i  i  i  i  i  i  i  i  i  i  i  i  i  i          \n",
      "       i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i       \n",
      "    i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i    \n",
      " k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k \n",
      " k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k \n",
      "    k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k    \n",
      "       k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k  k       \n",
      "          k  k  k  k  k  k  k  k  k  k  k  k  k  k  k          \n",
      "             k  k  k  k  k  k  k  k  k  k  k  k  k             \n",
      "                k  k  k  k  k  k  k  k  k  k  k                \n",
      "                   k  k  k  k  k  k  k  k  k                   \n",
      "                      k  k  k  k  k  k  k                      \n",
      "                         k  k  k  k  k                         \n",
      "                            k  k  k                            \n",
      "                               k                               \n",
      "\n"
     ]
    }
   ],
   "source": [
    "z= ''\n",
    "for i in range (0,11):\n",
    "    if i < 10:\n",
    "        for j in range (0, 21):\n",
    "            if j >= 10-i and j <= 10+i:\n",
    "                z += ' i '\n",
    "            else: \n",
    "                z += '   '    \n",
    "        z += '\\n'\n",
    "    else:\n",
    "        for k in range (11,-1, -1):\n",
    "            for l in range (0, 21):\n",
    "                if l >= 10-k and l <= 10+k:\n",
    "                    z += ' k '\n",
    "                else: \n",
    "                    z += '   '    \n",
    "            z += '\\n'\n",
    "print (z)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               *                               \n",
      "                            *  *  *                            \n",
      "                         *  *  *  *  *                         \n",
      "                      *  *  *  *  *  *  *                      \n",
      "                   *  *  *  *  *  *  *  *  *                   \n",
      "                *  *  *  *  *  *  *  *  *  *  *                \n",
      "             *  *  *  *  *  *  *  *  *  *  *  *  *             \n",
      "          *  *  *  *  *  *  *  *  *  *  *  *  *  *  *          \n",
      "       *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *       \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *    \n",
      " *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *    \n",
      "       *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *       \n",
      "          *  *  *  *  *  *  *  *  *  *  *  *  *  *  *          \n",
      "             *  *  *  *  *  *  *  *  *  *  *  *  *             \n",
      "                *  *  *  *  *  *  *  *  *  *  *                \n",
      "                   *  *  *  *  *  *  *  *  *                   \n",
      "                      *  *  *  *  *  *  *                      \n",
      "                         *  *  *  *  *                         \n",
      "                            *  *  *                            \n",
      "                               *                               \n",
      "\n"
     ]
    }
   ],
   "source": [
    "z= ''\n",
    "for i in range (0,11):\n",
    "    if i < 10:\n",
    "        for j in range (0, 21):\n",
    "            if j >= 10-i and j <= 10+i:\n",
    "                z += ' * '\n",
    "            else: \n",
    "                z += '   '    \n",
    "        z += '\\n'\n",
    "    else:\n",
    "        for k in range (10,-1, -1):\n",
    "            for l in range (0, 21):\n",
    "                if l >= 10-k and l <= 10+k:\n",
    "                    z += ' * '\n",
    "                else: \n",
    "                    z += '   '    \n",
    "            z += '\\n'\n",
    "print (z)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan jumlah bintang:8\n",
      " *  *  *  *  *  *  *  * \n",
      " *  *  *  *  *  *  * \n",
      " *  *  *  *  *  * \n",
      " *  *  *  *  * \n",
      " *  *  *  * \n",
      " *  *  * \n",
      " *  * \n",
      " *                      \n",
      " *  *                   \n",
      " *  *  *                \n",
      " *  *  *  *             \n",
      " *  *  *  *  *          \n",
      " *  *  *  *  *  *       \n",
      " *  *  *  *  *  *  *    \n",
      " *  *  *  *  *  *  *  * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#solve it 2 - final\n",
    "jawal=int(input(\"Masukan jumlah bintang:\"))\n",
    "\n",
    "a=''\n",
    "\n",
    "j=jawal\n",
    "\n",
    "for relement in range(0,j):\n",
    "    if j>1:\n",
    "        for celement in range (0,j):\n",
    "            a+=' * '\n",
    "        j-=1\n",
    "        a+='\\n'\n",
    "    else:\n",
    "        j=jawal\n",
    "        for relement in range (0,j):\n",
    "            for celement in range(0,j):\n",
    "                if celement<=relement:\n",
    "                    a+=' * '\n",
    "                else:\n",
    "                    a+='   '\n",
    "            a+='\\n'\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       *  *       \n",
      "    *  *  *  *    \n",
      " *  *  *  *  *  * \n",
      "    *  *  *  *    \n",
      "       *  *       \n",
      "                  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#solve it 5\n",
    "j=6\n",
    "a=''\n",
    "\n",
    "center1=int(j/2-1)\n",
    "center2=int(j/2)\n",
    "\n",
    "for relement in range (0,j):\n",
    "    if relement<center2:\n",
    "        \n",
    "        for celement in range (0,j):\n",
    "            if celement>=center1-relement and celement<=center2+relement:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                a+='   '\n",
    "        a+='\\n'\n",
    "    else:\n",
    "        for celement in range(0,j):\n",
    "            if celement>relement-center2 and celement<j-relement+center1:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                a+='   '\n",
    "        a+='\\n'\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan Angka:16\n",
      "                      *  *                      \n",
      "                   *  *  *  *                   \n",
      "                *  *  *  *  *  *                \n",
      "             *  *  *  *  *  *  *  *             \n",
      "          *  *  *  *  *  *  *  *  *  *          \n",
      "       *  *  *  *  *  *  *  *  *  *  *  *       \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  *    \n",
      " *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * \n",
      " *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  *    \n",
      "       *  *  *  *  *  *  *  *  *  *  *  *       \n",
      "          *  *  *  *  *  *  *  *  *  *          \n",
      "             *  *  *  *  *  *  *  *             \n",
      "                *  *  *  *  *  *                \n",
      "                   *  *  *  *                   \n",
      "                      *  *                      \n",
      "                                                \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#solveit5gakrapi\n",
    "\n",
    "a=''\n",
    "angka=int(input(\"Masukan Angka:\"))\n",
    "\n",
    "if angka%2==0:\n",
    "    center1=int(angka/2-1)\n",
    "    center2=int(angka/2)\n",
    "\n",
    "    for relement in range (0,angka+1):\n",
    "        if relement<center2:\n",
    "            for celement in range (0,angka):\n",
    "                if celement>=center1-relement and celement<=center2+relement:\n",
    "                    a+=' * '\n",
    "                else:\n",
    "                    a+='   '\n",
    "            a+='\\n'\n",
    "        else:\n",
    "            for celement in range(0,angka):\n",
    "                if celement>relement-1-center2 and celement<angka-relement+center1+1:\n",
    "                    a+=' * '\n",
    "                else:\n",
    "                    a+='   '\n",
    "            a+='\\n'\n",
    "    print(a)\n",
    "\n",
    "else:\n",
    "\n",
    "    center=int((angka+1)/2)-1\n",
    "\n",
    "    for relement in range(0,angka+1):\n",
    "        for celement in range (0,angka):\n",
    "            if relement<=center:\n",
    "                if celement>=center-relement and celement<=center+relement:\n",
    "                    a+=' * '\n",
    "                else:\n",
    "                    a+='   ' \n",
    "            elif relement==center+1:\n",
    "                a+=' * '\n",
    "            else:\n",
    "                if celement>=relement-1-center and celement<angka-relement+1+center:\n",
    "                    a+=' * '\n",
    "                else:\n",
    "                    a+='   '\n",
    "        a+='\\n'\n",
    "                \n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " i  i  i  i  i  i  i  i  i  i  *  i  i  i  i  i  i  i  i  i  i \n",
      " i  i  i  i  i  i  i  i  i  *  *  *  i  i  i  i  i  i  i  i  i \n",
      " i  i  i  i  i  i  i  i  *  *  *  *  *  i  i  i  i  i  i  i  i \n",
      " i  i  i  i  i  i  i  *  *  *  *  *  *  *  i  i  i  i  i  i  i \n",
      " i  i  i  i  i  i  *  *  *  *  *  *  *  *  *  i  i  i  i  i  i \n",
      " i  i  i  i  i  *  *  *  *  *  *  *  *  *  *  *  i  i  i  i  i \n",
      " i  i  i  i  *  *  *  *  *  *  *  *  *  *  *  *  *  i  i  i  i \n",
      " i  i  i  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  i  i  i \n",
      " i  i  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  i  i \n",
      " i  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  i \n",
      "\n"
     ]
    }
   ],
   "source": [
    "z= ''\n",
    "for i in range (0,10,1):\n",
    "    for j in range (0, 21):\n",
    "        if j >= 10-i and j <= 10+i:\n",
    "            z += ' * '\n",
    "        else: \n",
    "            z += ' i '\n",
    "    z += '\\n'\n",
    "print (z) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan Besar Bintang: 5\n",
      " *  *  *  *  *  *  *  *  * \n",
      " *  *  *  *  i  *  *  *  * \n",
      " *  *  *  i  i  i  *  *  * \n",
      " *  *  i  i  i  i  i  *  * \n",
      " *  i  i  i  i  i  i  i  * \n",
      " *  *  z  z  z  z  z  *  * \n",
      " *  *  *  z  z  z  *  *  * \n",
      " *  *  *  *  z  *  *  *  * \n",
      " *  *  *  *  *  *  *  *  * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "size = int(input('Masukkan Besar Bintang: '))\n",
    "z = ''\n",
    "for j in range (size+1):\n",
    "    if j < size:\n",
    "        for k in range (1,size*2):\n",
    "            if k <=size-j or k >= size+j:\n",
    "                z += ' * '\n",
    "            else:\n",
    "                z += ' i '\n",
    "        z += '\\n'            \n",
    "    else:\n",
    "        for l in range (size-1, 0, -1): #ukurannya dikurangin 2 dari ukuran j, soalnya kan emg turun 1 baris dan baris yg terakhir di j itu dipake buat bikin else\n",
    "            for m in range (1,size*2):\n",
    "                if m <=size-l+1 or m >=size+l-1:\n",
    "                    z += ' * '\n",
    "                else:\n",
    "                    z += ' z '\n",
    "            z += '\\n'\n",
    "\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan jumlah baris segitiga:5\n",
      "                           \n",
      "             *  *          \n",
      "          *  *  *  *       \n",
      "       *  *  *  *  *  *    \n",
      "    *  *  *  *  *  *  *  * \n",
      " *  *  *  *  *  *  *  *  * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#solveit3\n",
    "\n",
    "a=''\n",
    "\n",
    "baris=int(input(\"Masukan jumlah baris segitiga:\"))\n",
    "kolom=(baris-1)*2+1\n",
    "\n",
    "for relement in range(0,baris+1):\n",
    "    for celement in range(0,kolom):\n",
    "        if celement>=baris-relement and celement<baris+relement:\n",
    "            a+=' * '\n",
    "        else:\n",
    "            a+='   '\n",
    "    a+='\\n'\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               *                               \n",
      "                            *  *  *                            \n",
      "                         *  *  *  *  *                         \n",
      "                      *  *  *  *  *  *  *                      \n",
      "                   *  *  *  *  *  *  *  *  *                   \n",
      "                *  *  *  *  *  *  *  *  *  *  *                \n",
      "             *  *  *  *  *  *  *  *  *  *  *  *  *             \n",
      "          *  *  *  *  *  *  *  *  *  *  *  *  *  *  *          \n",
      "       *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *       \n",
      "    *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *    \n",
      "\n"
     ]
    }
   ],
   "source": [
    "z= ''\n",
    "for i in range (0,10):\n",
    "    for j in range (0, 21):\n",
    "        if j >= 10-i and j <= 10+i:\n",
    "            z += ' * '\n",
    "        else: \n",
    "            z += '   '    \n",
    "    z += '\\n'\n",
    "print (z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def kali(s,x,a):\n",
    "    if (x<2):\n",
    "        return 1\n",
    "    else:\n",
    "        return (x*tiga(x,a))\n",
    "    \n",
    "def tiga(x,a):\n",
    "    if a==3:\n",
    "        s = 5*a\n",
    "        return s\n",
    "    else:\n",
    "        return x*a\n",
    "\n",
    "print(kali(5,3))\n",
    "print (s)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
