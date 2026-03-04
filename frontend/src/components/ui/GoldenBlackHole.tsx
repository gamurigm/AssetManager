"use client";

import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Sparkles } from '@react-three/drei';
import * as THREE from 'three';

// ─── Accretion Disk (golden smooth torus cloud) ─────────────────────
const PARTICLE_COUNT = 3000;
const RING_R = 3.2;
const TUBE_R = 1.0;

const diskParticles = Array.from({ length: PARTICLE_COUNT }, () => {
    const u = Math.random() * Math.PI * 2;
    const v = Math.random() * Math.PI * 2;
    const x = (RING_R + TUBE_R * Math.cos(v)) * Math.cos(u);
    const y = TUBE_R * Math.sin(v) * 0.08; // ultra-flat disk
    const z = (RING_R + TUBE_R * Math.cos(v)) * Math.sin(u);
    const distance = Math.sqrt(x * x + z * z);
    const speed = (8 / distance) * (Math.random() * 0.4 + 0.6);
    const scale = Math.random() * 0.6 + 0.4;
    return { basePosition: new THREE.Vector3(x, y, z), speed, scale, distance };
});

function AccretionDisk() {
    const groupRef = useRef<THREE.Group>(null);
    const meshRef = useRef<THREE.InstancedMesh>(null);

    useFrame((state) => {
        if (!groupRef.current || !meshRef.current) return;
        const t = state.clock.getElapsedTime();

        // Gentle tilt breathing
        groupRef.current.rotation.y = t * 0.12;
        groupRef.current.rotation.x = 0.35 + Math.sin(t * 0.15) * 0.03;

        const dummy = new THREE.Object3D();
        diskParticles.forEach((p, i) => {
            const angle = Math.atan2(p.basePosition.z, p.basePosition.x) + t * p.speed * 0.3;
            const r = p.distance;
            const yWarp = Math.sin(t * 1.5 + r * 1.2) * 0.06;

            dummy.position.set(Math.cos(angle) * r, p.basePosition.y + yWarp, Math.sin(angle) * r);
            const pulse = (Math.sin(t * 3 + i * 0.01) * 0.3 + 0.7) * p.scale;
            dummy.scale.setScalar(pulse);
            dummy.updateMatrix();
            meshRef.current?.setMatrixAt(i, dummy.matrix);

            // Neon gradient: white-hot center → golden → tomato → crimson edge
            const color = new THREE.Color();
            const nd = Math.max(0, Math.min(1, (r - 2.2) / 3.0));

            if (nd < 0.3) {
                // Inner: white-hot → bright gold
                color.lerpColors(new THREE.Color('#fff8e1'), new THREE.Color('#ffd700'), nd / 0.3);
            } else if (nd < 0.65) {
                // Mid: gold → neon tomato/orange
                color.lerpColors(new THREE.Color('#ffd700'), new THREE.Color('#ff6347'), (nd - 0.3) / 0.35);
            } else {
                // Outer: tomato → deep crimson red
                color.lerpColors(new THREE.Color('#ff6347'), new THREE.Color('#dc143c'), (nd - 0.65) / 0.35);
            }
            meshRef.current?.setColorAt(i, color);
        });

        meshRef.current.instanceMatrix.needsUpdate = true;
        if (meshRef.current.instanceColor) meshRef.current.instanceColor.needsUpdate = true;
    });

    return (
        <group ref={groupRef}>
            <instancedMesh ref={meshRef} args={[undefined, undefined, PARTICLE_COUNT]}>
                <sphereGeometry args={[0.03, 6, 6]} />
                <meshStandardMaterial
                    toneMapped={false}
                    emissive="#ff8c00"
                    emissiveIntensity={3}
                    transparent
                    opacity={0.9}
                    blending={THREE.AdditiveBlending}
                    depthWrite={false}
                />
            </instancedMesh>
        </group>
    );
}

// ─── Expanding Harmonic Waves ───────────────────────────────────────
function ExpandingWaves() {
    const wavesRef = useRef<THREE.Group>(null);
    const WAVE_COUNT = 5;

    useFrame((state) => {
        if (!wavesRef.current) return;
        const t = state.clock.getElapsedTime();
        wavesRef.current.children.forEach((ring, i) => {
            const phase = (t * 0.4 + i * (Math.PI * 2 / WAVE_COUNT)) % (Math.PI * 2);
            const progress = phase / (Math.PI * 2); // 0 → 1
            const scale = 2.5 + progress * 6;
            ring.scale.set(scale, scale, scale);
            (ring as THREE.Mesh).material = (ring as THREE.Mesh).material as THREE.MeshBasicMaterial;
            ((ring as THREE.Mesh).material as THREE.MeshBasicMaterial).opacity = (1 - progress) * 0.25;
        });
    });

    return (
        <group ref={wavesRef} rotation={[Math.PI / 2 + 0.35, 0, 0]}>
            {Array.from({ length: WAVE_COUNT }).map((_, i) => (
                <mesh key={i}>
                    <ringGeometry args={[0.98, 1.0, 128]} />
                    <meshBasicMaterial
                        color="#ff8c00"
                        side={THREE.DoubleSide}
                        transparent
                        opacity={0}
                        blending={THREE.AdditiveBlending}
                        depthWrite={false}
                    />
                </mesh>
            ))}
        </group>
    );
}

// ─── Distant Stars (subtle, sparse, beautiful) ─────────────────────
function DistantStars() {
    const ref = useRef<THREE.Points>(null);
    const COUNT = 1200;

    const [positions, colors] = useMemo(() => {
        const pos = new Float32Array(COUNT * 3);
        const col = new Float32Array(COUNT * 3);
        const c = new THREE.Color();

        for (let i = 0; i < COUNT; i++) {
            const r = 40 + Math.random() * 40;
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(2 * Math.random() - 1);
            pos[i * 3] = r * Math.sin(phi) * Math.cos(theta);
            pos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
            pos[i * 3 + 2] = r * Math.cos(phi);

            const rnd = Math.random();
            if (rnd > 0.85) c.set('#aaddff');
            else if (rnd > 0.5) c.set('#ffffff');
            else if (rnd > 0.2) c.set('#ffe8c0');
            else c.set('#ffcc88');
            col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b;
        }
        return [pos, col];
    }, []);

    useFrame((state) => {
        if (ref.current) ref.current.rotation.y = state.clock.getElapsedTime() * 0.008;
    });

    return (
        <points ref={ref}>
            <bufferGeometry>
                <bufferAttribute attach="attributes-position" args={[positions, 3]} />
                <bufferAttribute attach="attributes-color" args={[colors, 3]} />
            </bufferGeometry>
            <pointsMaterial size={0.12} vertexColors transparent opacity={0.7} sizeAttenuation />
        </points>
    );
}

// ─── Distant Galaxies (colorful nebula clusters far away) ───────────
const GALAXY_CONFIGS = [
    { pos: [-35, 12, -50], color: '#7c3aed', count: 120, spread: 3.5 },   // violet
    { pos: [40, -8, -55], color: '#3b82f6', count: 100, spread: 2.8 },    // blue
    { pos: [-20, -15, -60], color: '#ec4899', count: 80, spread: 2.2 },   // pink
    { pos: [28, 20, -45], color: '#06b6d4', count: 90, spread: 3.0 },     // cyan
    { pos: [-45, 5, -40], color: '#f59e0b', count: 70, spread: 2.0 },     // amber
    { pos: [50, -20, -50], color: '#10b981', count: 60, spread: 1.8 },    // emerald
];

function DistantGalaxies() {
    const ref = useRef<THREE.Group>(null);

    useFrame((state) => {
        if (ref.current) ref.current.rotation.y = state.clock.getElapsedTime() * 0.005;
    });

    return (
        <group ref={ref}>
            {GALAXY_CONFIGS.map((g, gi) => (
                <GalaxyCluster key={gi} position={g.pos as [number, number, number]} color={g.color} count={g.count} spread={g.spread} />
            ))}
        </group>
    );
}

function GalaxyCluster({ position, color, count, spread }: { position: [number, number, number]; color: string; count: number; spread: number }) {
    const positions = useMemo(() => {
        const pos = new Float32Array(count * 3);
        for (let i = 0; i < count; i++) {
            // Spiral-ish distribution
            const angle = (i / count) * Math.PI * 4 + Math.random() * 0.5;
            const r = Math.random() * spread;
            const height = (Math.random() - 0.5) * spread * 0.2;
            pos[i * 3] = Math.cos(angle) * r + (Math.random() - 0.5) * 0.5;
            pos[i * 3 + 1] = height;
            pos[i * 3 + 2] = Math.sin(angle) * r + (Math.random() - 0.5) * 0.5;
        }
        return pos;
    }, [count, spread]);

    return (
        <group position={position}>
            <points>
                <bufferGeometry>
                    <bufferAttribute attach="attributes-position" args={[positions, 3]} />
                </bufferGeometry>
                <pointsMaterial
                    size={0.2}
                    color={color}
                    transparent
                    opacity={0.6}
                    blending={THREE.AdditiveBlending}
                    depthWrite={false}
                    sizeAttenuation
                />
            </points>
            {/* Soft glow core */}
            <mesh>
                <sphereGeometry args={[0.6, 16, 16]} />
                <meshBasicMaterial color={color} transparent opacity={0.08} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>
        </group>
    );
}

// ─── Photon Rings (layered golden glow) ─────────────────────────────
function PhotonRings() {
    const ref = useRef<THREE.Group>(null);

    useFrame((state) => {
        if (ref.current) {
            ref.current.rotation.z = state.clock.getElapsedTime() * 0.15;
            ref.current.rotation.y = Math.sin(state.clock.getElapsedTime() * 0.3) * 0.05;
        }
    });

    return (
        <group ref={ref}>
            {/* Super bright inner boundary (Photon Sphere) */}
            <mesh rotation={[Math.PI / 2, 0, 0]}>
                <torusGeometry args={[1.81, 0.02, 16, 128]} />
                <meshBasicMaterial color="#ffffff" transparent opacity={0.9} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>

            {/* Orbiting string of golden energy */}
            <mesh rotation={[Math.PI / 2 + 0.15, 0.05, 0.2]}>
                <torusGeometry args={[1.85, 0.012, 16, 128]} />
                <meshBasicMaterial color="#ffd700" transparent opacity={0.8} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>

            {/* Orbiting string of neon tomato energy */}
            <mesh rotation={[Math.PI / 2 - 0.1, 0.15, -0.1]}>
                <torusGeometry args={[1.92, 0.01, 16, 128]} />
                <meshBasicMaterial color="#ff6347" transparent opacity={0.6} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>

            {/* Faint outer crimson orbit */}
            <mesh rotation={[Math.PI / 2 + 0.05, -0.1, 0.3]}>
                <torusGeometry args={[2.0, 0.005, 16, 128]} />
                <meshBasicMaterial color="#dc143c" transparent opacity={0.4} blending={THREE.AdditiveBlending} depthWrite={false} />
            </mesh>
        </group>
    );
}

// ─── Main Scene ─────────────────────────────────────────────────────
export default function GoldenBlackHole() {
    return (
        <div className="absolute inset-0 w-full h-full overflow-hidden z-0" style={{ background: '#030308' }}>
            {/* Distant nebula glow via CSS — colorful galaxy halos */}
            <div className="absolute inset-0 pointer-events-none" style={{
                background: `
                    radial-gradient(ellipse 30% 25% at 12% 18%, rgba(124, 58, 237, 0.12) 0%, transparent 70%),
                    radial-gradient(ellipse 25% 20% at 88% 72%, rgba(59, 130, 246, 0.10) 0%, transparent 70%),
                    radial-gradient(ellipse 20% 18% at 22% 80%, rgba(236, 72, 153, 0.08) 0%, transparent 70%),
                    radial-gradient(ellipse 28% 22% at 75% 15%, rgba(6, 182, 212, 0.09) 0%, transparent 70%),
                    radial-gradient(ellipse 18% 15% at 8% 55%, rgba(245, 158, 11, 0.07) 0%, transparent 70%),
                    radial-gradient(ellipse 22% 18% at 90% 45%, rgba(16, 185, 129, 0.06) 0%, transparent 70%),
                    radial-gradient(ellipse 60% 50% at 50% 50%, rgba(200, 160, 50, 0.03) 0%, transparent 60%)
                `
            }} />

            <Canvas camera={{ position: [0, 2.5, 9], fov: 55 }} gl={{ antialias: true, alpha: false }}>
                <color attach="background" args={['#030308']} />
                <ambientLight intensity={0.15} />
                <pointLight position={[0, 0, 0]} intensity={60} color="#ff8c00" distance={15} />

                {/* Distant subtle stars */}
                <DistantStars />

                {/* Distant colorful galaxies */}
                <DistantGalaxies />

                {/* Expanding harmonic wave pulses */}
                <ExpandingWaves />

                {/* Event Horizon */}
                <mesh>
                    <sphereGeometry args={[1.8, 64, 64]} />
                    <meshBasicMaterial color="#000000" />
                </mesh>

                {/* Golden accretion disk */}
                <AccretionDisk />

                {/* Tiny sparkles — ambient neon dust */}
                <Sparkles count={150} scale={12} size={1.2} speed={0.3} opacity={0.15} color="#ff8c00" />

                <OrbitControls
                    enableZoom={false}
                    enablePan={false}
                    autoRotate
                    autoRotateSpeed={0.4}
                    maxPolarAngle={Math.PI / 2 + 0.25}
                    minPolarAngle={Math.PI / 2 - 0.35}
                />
            </Canvas>
        </div>
    );
}
