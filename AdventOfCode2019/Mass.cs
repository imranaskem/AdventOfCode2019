using System;
using System.Collections.Generic;
using System.Text;

namespace AdventOfCode2019
{
    class Mass
    {
        private readonly int _mass;

        public Mass(int mass)
        {
            this._mass = mass;
        }

        public static Mass FromString(string line)
        {
            if (int.TryParse(line, out var parsedInt))
            {
                return new Mass(parsedInt);
            }

            throw new ArgumentException($"Failed to parse integer from {line}");
        }
    }
}
