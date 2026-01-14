#!/usr/bin/env bash
set -e

OUTDIR=${1:-graphs}
NMIN=${2:-4}
NMAX=${3:-10}
MAXDEG=${4:-3}

mkdir -p "$OUTDIR"

for n in $(seq $NMIN $NMAX); do
  echo "Generating n=$n (max degree $MAXDEG)..."
  geng -D${MAXDEG} $n -q > "${OUTDIR}/graphs_n${n}_D${MAXDEG}.g6"
done

echo "Done. Generated files in $OUTDIR"
