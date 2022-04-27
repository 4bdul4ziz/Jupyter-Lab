import java.util.*
import kotlin.math.min

class KMeans(val nclusters: Int, val ndims: Int, val npoints: Int, val maxiters: Int, seed: Long? = null) {
    init {
        if (nclusters < 1) throw IllegalArgumentException("nclusters < 1")
        if (ndims < 1) throw IllegalArgumentException("ndims < 1")
        if (npoints < 1) throw IllegalArgumentException("npoints < 1")
        if (maxiters < 1) throw IllegalArgumentException("maxiters < 1")
    }

    private val rand = if (seed == null) Random() else Random(seed)
    val clusters = IntArray(npoints)
    val centers = FloatArray(ndims * nclusters)

    private val counts = IntArray(nclusters)
    private val distances = FloatArray(npoints)

    private var data = floatArrayOf()

    fun fit(data: FloatArray): Boolean {
        if (data.size % ndims != 0) throw IllegalArgumentException("data.size % ndims != 0")

        this.data = data

        init()

        for (ii in 0 until maxiters) {
            updateClusters()
            updateCenters()
        }

        return false
    }

    /** Initialize cluster centers with K-Means++. */
    private fun init() {
        distances.fill(Float.POSITIVE_INFINITY)

        initCluster(0, rand.nextInt(npoints))

        for (ic in 1 until nclusters) {
            var s = 0f
            for (ip in 0 until npoints) {
                val dist = distance2(ip, ic - 1)
                distances[ip] = min(distances[ip], dist)
                s += distances[ip]
            }

            val r = rand.nextFloat() * s
            s = 0f
            for (ip in 0 until npoints) {
                s += distances[ip]
                if (r < s) {
                    initCluster(ic, ip)
                    break
                }
            }

        }
    }

    /** Initialize cluster center with a data point. */
    private fun initCluster(ic: Int, ip: Int) {
        System.arraycopy(data, ndims * ip, centers, ndims * ic, ndims)
    }

    /** Recompute cluster assignments from cluster centers. */
    private fun updateClusters() {
        counts.fill(0)
        for (ip in 0 until npoints) {
            val ic = findNearestCluster(ip)
            clusters[ip] = ic
            counts[ic]++
        }
    }

    /** Recompute cluster centers from cluster assignments. */
    private fun updateCenters() {
        centers.fill(0f)
        for (ip in 0 until npoints) {
            val ic = clusters[ip]
            for (id in 0 until ndims) {
                centers[ndims * ic + id] += data[ndims * ip + id] / counts[ic]
            }
        }
    }

    /** Find the nearest cluster to the point. */
    private fun findNearestCluster(ip: Int): Int {
        var mindist = Float.POSITIVE_INFINITY
        var minic = 0
        for (ic in 0 until nclusters) {
            val dist = distance2(ip, ic)
            if (dist < mindist) {
                mindist = dist
                minic = ic
            }
        }
        return minic
    }

    /** Squared distance between a data point and a cluster center. */
    private fun distance2(ip: Int, ic: Int): Float {
        var s = 0f
        for (id in 0 until ndims) {
            val t = data[ndims * ip + id] - centers[ndims * ic + id]
            s += t * t
        }
        return s
    }
}
